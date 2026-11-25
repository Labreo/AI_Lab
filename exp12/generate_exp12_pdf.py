import os
import re
import html
import pexpect
import fitz
from PIL import Image, ImageDraw, ImageFont
import pygments
from pygments.lexers import PrologLexer
from pygments.token import Token

FONT_PATH = '/System/Library/Fonts/Menlo.ttc'
HEADER_IMAGE_PATH = 'assets/gec_header.png'
PROMPT = '(base) sanjaywaradkar@Sanjays-MacBook-Air-2 AI_Lab % '
LINES_PER_PAGE = 60

def get_token_color(ttype):
    if ttype in Token.Keyword or ttype in Token.Keyword.Constant or \
       ttype in Token.Keyword.Declaration or ttype in Token.Keyword.Namespace or \
       ttype in Token.Keyword.Pseudo or ttype in Token.Keyword.Reserved or \
       ttype in Token.Operator.Word:
        return (0, 0, 255)
    elif ttype in Token.String or ttype in Token.String.Doc or \
         ttype in Token.String.Interpol or ttype in Token.String.Single or \
         ttype in Token.String.Double or ttype in Token.String.Char:
        return (163, 21, 21)
    elif ttype in Token.Number or ttype in Token.Number.Integer or ttype in Token.Number.Float:
        return (9, 134, 88)
    elif ttype in Token.Comment or ttype in Token.Comment.Single or \
         ttype in Token.Comment.Multiline or ttype in Token.Comment.Hashbang:
        return (0, 128, 0)
    else:
        return (0, 0, 0)

def render_code_single_column(code_str, font_size=20, line_height=30, pad_x=20, pad_y=16, lexer=None):
    font = ImageFont.truetype(FONT_PATH, font_size)
    lines = code_str.splitlines()
    char_w = font.getlength('m')
    max_line_len = max(len(l) for l in lines) if lines else 20
    img_w = int(max_line_len * char_w + pad_x * 2 + 30)
    img_h = int(len(lines) * line_height + pad_y * 2)
    
    im = Image.new('RGB', (img_w, img_h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    guide_color = (230, 230, 230)
    indents = [(len(l) - len(l.lstrip(' '))) if l.strip() else 0 for l in lines]
    for col in [4, 8, 12, 16, 20]:
        for r, ind in enumerate(indents):
            if ind >= col:
                gx = int(pad_x + col * char_w)
                gy1 = int(pad_y + r * line_height)
                gy2 = int(pad_y + (r + 1) * line_height)
                draw.line([(gx, gy1), (gx, gy2)], fill=guide_color, width=1)
                
    tokens = list(pygments.lex(code_str, lexer or PrologLexer()))
    x = pad_x
    y = pad_y
    for ttype, val in tokens:
        if '\n' in val:
            parts = val.split('\n')
            for idx, p in enumerate(parts):
                if p:
                    col = get_token_color(ttype)
                    draw.text((x, y), p, font=font, fill=col)
                    x += int(font.getlength(p))
                if idx < len(parts) - 1:
                    x = pad_x
                    y += line_height
        else:
            col = get_token_color(ttype)
            draw.text((x, y), val, font=font, fill=col)
            x += int(font.getlength(val))
            
    return im

def render_terminal_screenshot(terminal_text, font_size=20, line_height=29, pad_x=20, pad_y=16):
    font = ImageFont.truetype(FONT_PATH, font_size)
    lines = [l.expandtabs(8) for l in terminal_text.splitlines()]
    char_w = font.getlength('m')
    max_line_len = max(len(l) for l in lines) if lines else 20
    img_w = int(max_line_len * char_w + pad_x * 2 + 30)
    img_h = int(len(lines) * line_height + pad_y * 2)
    
    im = Image.new('RGB', (img_w, img_h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    x = pad_x
    y = pad_y
    for l in lines:
        draw.text((x, y), l, font=font, fill=(0, 0, 0))
        y += line_height
        
    return im

def paginate_code(lines, per_page=80, lookback=25):
    pages = []
    start = 0
    while len(lines) - start > per_page:
        cut = start + per_page
        for idx in range(cut, cut - lookback, -1):
            if not lines[idx - 1].strip() or lines[idx - 1].strip().endswith('.'):
                cut = idx
                break
        pages.append(lines[start:cut])
        start = cut
    pages.append(lines[start:])
    return pages

def run_prolog_session(script, lines):
    chunks = []
    child = pexpect.spawn('swipl', [script], encoding='utf-8', timeout=20,
                          env={**os.environ, 'TERM': 'dumb'})
    child.logfile_read = type('Log', (), {'write': lambda s, x: chunks.append(x), 'flush': lambda s: None})()
    for line in lines:
        child.expect([r'\?- ', r'\|: '])
        child.sendline(line)
    child.expect(pexpect.EOF)
    text = re.sub(r'\x1b\[[0-9;?]*[A-Za-z]', '', ''.join(chunks).replace('\r', ''))
    text = text.rstrip()
    if text.endswith('?-'):
        text += ' ' + lines[-1]
    return PROMPT + 'swipl ' + script + '\n' + text

def create_kanak_pdf():
    doc = fitz.open()
    tmp = 'temp_page.png'

    def add_page(label, img):
        page = doc.new_page(width=612, height=792)
        page.insert_image(fitz.Rect(184.875, 22.5, 427.125, 52.5), filename=HEADER_IMAGE_PATH)
        page.insert_text(fitz.Point(72.0, 80.0), label, fontname='times-bold', fontsize=12.0)
        img.save(tmp)
        w, h = img.size
        target_w = 468.0
        target_h = target_w * (h / w)
        max_h = 750.0 - 89.37
        if target_h > max_h:
            target_h = max_h
            target_w = target_h * (w / h)
        x0 = 72.0
        page.insert_image(fitz.Rect(x0, 89.37, x0 + target_w, 89.37 + target_h), filename=tmp)
        if os.path.exists(tmp):
            os.remove(tmp)

    configs = [
        ('exp12/first_aid.pl', [
            'go.', 'Cough unable to speak', 'yes',
            'go.', 'burn', 'yes',
            'halt.'
        ]),
        ('exp12/nutritional_deficiency.pl', [
            'go.', 'unusually tired', 'yes',
            'go.', 'bleeding gums', 'yes',
            'halt.'
        ]),
        ('exp12/fitness_expert.pl', [
            'go.', 'weight loss', 'no', 'no',
            'go.', 'muscle gain', 'yes', 'no',
            'halt.'
        ]),
        ('exp12/eye_conditions.pl', [
            'go.', 'red and itchy', 'yes',
            'go.', 'blurred vision', 'yes',
            'halt.'
        ])
    ]

    for script, inputs in configs:
        base = os.path.basename(script)
        with open(script) as f:
            code = f.read().rstrip('\n')
        lines = code.splitlines(keepends=True)
        chunks = paginate_code(lines, per_page=80, lookback=25)
        code_imgs = [render_code_single_column(''.join(c).rstrip('\n'), font_size=20, line_height=30) for c in chunks]
        
        # Max width padding for uniform scaling
        max_w = max(im.width for im in code_imgs)
        padded_imgs = []
        for im in code_imgs:
            canvas = Image.new('RGB', (max_w, im.height), (255, 255, 255))
            canvas.paste(im, (0, 0))
            padded_imgs.append(canvas)
            
        for i, img in enumerate(padded_imgs):
            lbl = f'Code ({base}):' if i == 0 else f'Code ({base}, continued):'
            add_page(lbl, img)
            
        term_text = run_prolog_session(script, inputs)
        term_img = render_terminal_screenshot(term_text, font_size=20, line_height=29)
        add_page(f'Output ({base}):', term_img)

    pdf_path = 'exp12/Kanak_exp12_AI.pdf'
    page_count = len(doc)
    doc.save(pdf_path, deflate=True, garbage=4, clean=True)
    doc.close()
    print(f'Successfully created {pdf_path} ({os.path.getsize(pdf_path)} bytes, {page_count} pages)')

def create_writeup_pdf():
    CSS = """
    body  { font-family: Times; font-size: 11pt; line-height: 1.25; }
    h1    { font-family: Times; font-size: 12.5pt; font-weight: bold; text-align: center; margin: 0 0 7pt 0; }
    h2    { font-family: Times; font-size: 11.5pt; font-weight: bold; margin: 8pt 0 2pt 0; }
    p     { margin: 0 0 4pt 0; text-align: justify; }
    li    { margin: 0 0 2pt 0; text-align: justify; }
    pre   { font-family: Courier; font-size: 9pt; line-height: 1.2; margin: 2pt 0 4pt 6pt; }
    .note { font-size: 9.5pt; font-style: italic; }
    """

    body_html = """
    <h1>Experiment 12: Program to Develop an Expert System using Prolog</h1>
    <h2>Aim:</h2>
    <ol>
    <li>Develop a Prolog-based expert system to recommend appropriate first-aid measures based on the observed injuries and symptoms.</li>
    <li>Develop a Prolog-based expert system to identify possible nutritional deficiencies based on the symptoms reported by the user.</li>
    <li>Develop a Prolog-based expert system to recommend suitable exercises based on the user's fitness goals and physical capabilities.</li>
    <li>Develop a Prolog-based expert system to identify possible eye conditions based on the symptoms reported by the user.</li>
    </ol>

    <h2>Theory:</h2>
    <p>An <b>expert system</b> is a computer program that holds the specialized domain knowledge of a human expert to provide advice, diagnostic evaluation, or reach conclusions in that domain. Its primary architectural components are:</p>
    <ul>
    <li><b>Knowledge base:</b> The domain knowledge, stored as declarative facts and IF–THEN inference rules.</li>
    <li><b>Inference engine:</b> Applies rules to known facts to deduce conclusions via forward chaining (data-driven) or backward chaining (goal-directed proof search).</li>
    <li><b>Working memory:</b> Stores dynamic facts established during the current consultation session (the user's recorded responses).</li>
    <li><b>User interface:</b> Interactively queries the user for unknown symptoms and displays conclusions alongside recommended advice.</li>
    </ul>
    <p>Prolog is exceptionally well-suited for expert systems because its built-in inference engine naturally performs <b>backward chaining with depth-first search and chronological backtracking</b>. Domain rules and facts form the knowledge base directly. For example, the clause</p>
    <pre>hypothesis(burn) :- verified(heat_injury), ask(blistered_skin, 'Is the skin red, painful or blistered').</pre>
    <p>reads: <i>"the condition is a burn IF the initial heat injury is verified AND blistered skin is confirmed."</i></p>

    <p><b>Working of the programs.</b> All four expert systems share a robust, standardized design:</p>
    <ul>
    <li><b>go/0</b> starts consultation. It prompts the user to enter their initial observed symptom, condition, or goal directly (with flexible keyword matching for free-form input).</li>
    <li><b>Hypotheses</b> use <i>verified/1</i> to match the user's initial assertion without interrogating unrelated conditions, then evaluate <i>ask/2</i> to prompt a targeted follow-up question only when relevant.</li>
    <li><b>ask/2</b> uses dynamic predicates <i>yes/1</i> and <i>no/1</i> as working memory so questions are never repeated in the same consultation.</li>
    <li><b>Re-assertion fallback:</b> If a condition is unconfirmed (e.g. follow-up answered 'no'), the consultation loop prompts the user to assert another symptom rather than asking arbitrary questions.</li>
    <li><b>undo/0</b> purges cached answers using <i>retractall/1</i> so subsequent sessions start with clean working memory.</li>
    </ul>

    <h2>Domain Implementations:</h2>
    <ol>
    <li><b>First aid (first_aid.pl):</b> Diagnoses 12 urgent injury conditions arranged from highest severity to minor traumas: <i>choking</i>, <i>severe bleeding</i>, <i>electric shock</i>, <i>heat stroke</i>, <i>snake bite</i>, <i>burn</i>, <i>fracture</i>, <i>concussion</i>, <i>sprain</i>, <i>chemical eye burn</i>, <i>minor cut</i>, and <i>nosebleed</i>. Provides step-by-step emergency care instructions.</li>
    <li><b>Nutritional deficiency (nutritional_deficiency.pl):</b> Identifies 12 nutritional and micronutrient deficiencies based on pathognomonic symptom pairs: <i>iron</i>, <i>vitamin C</i>, <i>vitamin D</i>, <i>vitamin B12</i>, <i>vitamin A</i>, <i>calcium</i>, <i>iodine</i>, <i>zinc</i>, <i>magnesium</i>, <i>potassium</i>, <i>folate</i>, and <i>protein deficiency</i>. Recommends targeted dietary foods and absorption guidance.</li>
    <li><b>Exercise recommendation (fitness_expert.pl):</b> Matches user goals (<i>weight loss</i>, <i>muscle gain</i>, <i>flexibility</i>, <i>endurance</i>, <i>core stability</i>, <i>stress relief</i>) and capabilities (<i>active status</i>, <i>joint pain</i>) to 15 exercise prescriptions: <i>brisk walking</i>, <i>running</i>, <i>swimming</i>, <i>cycling</i>, <i>bodyweight exercises</i>, <i>weight training</i>, <i>resistance bands</i>, <i>yoga</i>, <i>stretching</i>, <i>pilates</i>, <i>chair exercises</i>, <i>tai chi</i>, <i>deep breathing meditation</i>, <i>jump rope</i>, and <i>water aerobics</i>.</li>
    <li><b>Eye conditions (eye_conditions.pl):</b> Analyzes ocular symptoms to diagnose 12 ophthalmological conditions: <i>conjunctivitis</i>, <i>dry eye syndrome</i>, <i>refractive error</i>, <i>cataract</i>, <i>glaucoma</i>, <i>stye</i>, <i>corneal abrasion</i>, <i>blepharitis</i>, <i>subconjunctival hemorrhage</i>, <i>diabetic retinopathy</i>, <i>color blindness</i>, and <i>retinal detachment</i>, with clinical guidance on urgency.</li>
    </ol>
    <p class="note">These systems are educational demonstrations providing general guidance only, without replacing professional doctors or certified trainers.</p>

    <h2>Procedure:</h2>
    <ol>
    <li>Load the program with SWI-Prolog: <code>swipl &lt;program&gt;.pl</code></li>
    <li>Initiate consultation at prompt: <code>?- go.</code></li>
    <li>Enter the initial observed symptom, condition, or goal directly (e.g. <code>Cough unable to speak</code>, <code>burn</code>, <code>weight loss</code>, or type <code>list</code>).</li>
    <li>Answer the targeted follow-up question with <code>yes</code> or <code>no</code>.</li>
    <li>Inspect the diagnostic conclusion and advice. Type <code>halt.</code> to exit.</li>
    </ol>

    <h2>Result:</h2>
    <p>Each expert system was executed across distinct test scenarios, validating successful inference, interactive backtracking, working memory caching, and accurate recommendation generation as presented in the following execution pages.</p>
    """

    story = fitz.Story(html='<body>' + body_html + '</body>', user_css=CSS)
    tmp = 'exp12/exp12_writeup.pdf.tmp'
    writer = fitz.DocumentWriter(tmp)
    more = 1
    while more:
        device = writer.begin_page(fitz.Rect(0, 0, 612, 792))
        more, _ = story.place(fitz.Rect(72, 66, 540, 750))
        story.draw(device)
        writer.end_page()
    writer.close()
    
    doc = fitz.open(tmp)
    for page in doc:
        page.insert_image(fitz.Rect(184.875, 22.5, 427.125, 52.5), filename=HEADER_IMAGE_PATH)
    
    pdf_path = 'exp12/exp12_writeup.pdf'
    page_count = len(doc)
    doc.save(pdf_path, deflate=True, garbage=4)
    doc.close()
    os.remove(tmp)
    print(f'Successfully created {pdf_path} ({os.path.getsize(pdf_path)} bytes, {page_count} pages)')

def create_unified_pdf():
    doc = fitz.open('exp12/exp12_writeup.pdf')
    doc.insert_pdf(fitz.open('exp12/Kanak_exp12_AI.pdf'))
    pdf_path = 'exp12/exp12.pdf'
    page_count = len(doc)
    doc.save(pdf_path, deflate=True, garbage=4)
    doc.close()
    print(f'Successfully created {pdf_path} ({os.path.getsize(pdf_path)} bytes, {page_count} pages)')

if __name__ == '__main__':
    print('Generating Kanak_exp12_AI.pdf...')
    create_kanak_pdf()
    print('Generating exp12_writeup.pdf...')
    create_writeup_pdf()
    print('Generating exp12.pdf...')
    create_unified_pdf()
    print('All PDFs regenerated successfully!')
