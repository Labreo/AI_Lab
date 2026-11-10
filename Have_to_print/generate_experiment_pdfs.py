import os
import sys
import json
import shutil
import subprocess
import fitz
from PIL import Image, ImageDraw, ImageFont
import pygments
from pygments.lexers import PythonLexer, PrologLexer
from pygments.token import Token

FONT_PATH = '/System/Library/Fonts/Menlo.ttc'
HEADER_IMAGE_PATH = 'assets/gec_header.png'

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
    
    # Indent guides matching VS Code
    guide_color = (230, 230, 230)
    indents = [(len(l) - len(l.lstrip(' '))) if l.strip() else 0 for l in lines]
    for col in [4, 8, 12, 16, 20]:
        for r, ind in enumerate(indents):
            if ind >= col:
                gx = int(pad_x + col * char_w)
                gy1 = int(pad_y + r * line_height)
                gy2 = int(pad_y + (r + 1) * line_height)
                draw.line([(gx, gy1), (gx, gy2)], fill=guide_color, width=1)
                
    tokens = list(pygments.lex(code_str, lexer or PythonLexer()))
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

def render_code_two_columns(code_col1, code_col2, font_size=18, line_height=26, col_gap=50, pad_x=16, pad_y=14):
    im1 = render_code_single_column(code_col1, font_size, line_height, pad_x, pad_y)
    im2 = render_code_single_column(code_col2, font_size, line_height, pad_x, pad_y)
    
    total_w = im1.width + col_gap + im2.width
    total_h = max(im1.height, im2.height)
    
    composite = Image.new('RGB', (total_w, total_h), (255, 255, 255))
    composite.paste(im1, (0, 0))
    composite.paste(im2, (im1.width + col_gap, 0))
    
    # Subtle column divider
    draw = ImageDraw.Draw(composite)
    div_x = im1.width + col_gap // 2
    draw.line([(div_x, pad_y), (div_x, total_h - pad_y)], fill=(235, 235, 235), width=1)
    
    return composite

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

def create_experiment_pdf(pdf_path, code_img, term_img, is_two_col=False):
    doc = fitz.open()
    
    # Page 1: Code
    p1 = doc.new_page(width=612, height=792)
    # Header Image (centered, matching previous experiment PDFs)
    p1.insert_image(fitz.Rect(184.875, 22.5, 427.125, 52.5), filename=HEADER_IMAGE_PATH)
    # Section Label "Code:"
    p1.insert_text(fitz.Point(72.0, 80.0), 'Code:', fontname='times-bold', fontsize=12.0)
    
    temp_code_png = 'temp_code.png'
    code_img.save(temp_code_png)
    
    cw, ch = code_img.size
    if is_two_col:
        target_w = 512.0
        target_h = target_w * (ch / cw)
        max_h = 750.0 - 89.37
        if target_h > max_h:
            target_h = max_h
            target_w = target_h * (cw / ch)
        col_x = (612.0 - target_w) / 2.0
        p1.insert_image(fitz.Rect(col_x, 89.37, col_x + target_w, 89.37 + target_h), filename=temp_code_png)
    else:
        target_w = 468.0
        target_h = target_w * (ch / cw)
        max_h = 750.0 - 89.37
        if target_h > max_h:
            target_h = max_h
            target_w = target_h * (cw / ch)
        p1.insert_image(fitz.Rect(72.0, 89.37, 72.0 + target_w, 89.37 + target_h), filename=temp_code_png)
        
    # Page 2: Output
    p2 = doc.new_page(width=612, height=792)
    p2.insert_image(fitz.Rect(184.875, 22.5, 427.125, 52.5), filename=HEADER_IMAGE_PATH)
    p2.insert_text(fitz.Point(72.0, 80.0), 'Output:', fontname='times-bold', fontsize=12.0)
    
    temp_term_png = 'temp_term.png'
    term_img.save(temp_term_png)
    
    tw, th = term_img.size
    target_w = 468.0
    target_h = target_w * (th / tw)
    max_h = 750.0 - 89.37
    if target_h > max_h:
        target_h = max_h
        target_w = target_h * (tw / th)
    p2.insert_image(fitz.Rect(72.0, 89.37, 72.0 + target_w, 89.37 + target_h), filename=temp_term_png)
    
    doc.save(pdf_path, deflate=True, garbage=4, clean=True)
    doc.close()
    
    if os.path.exists(temp_code_png):
        os.remove(temp_code_png)
    if os.path.exists(temp_term_png):
        os.remove(temp_term_png)
    print(f'Successfully created {pdf_path} ({os.path.getsize(pdf_path)} bytes)')

PROMPT = '(base) sanjaywaradkar@Sanjays-MacBook-Air-2 AI_Lab % '
LINES_PER_PAGE = 60   # single-column code / terminal lines per page (matches Prim's / Dijkstra's)

# Runs a lab program with scripted stdin and echoes each answer after its prompt,
# so the captured text looks exactly like the interactive terminal session.
_ECHO_RUNNER = r"""
import builtins, json, runpy, sys
answers = iter(json.loads(sys.argv[2]))
def _input(prompt=''):
    value = next(answers)
    sys.stdout.write(str(prompt) + value + '\n')
    return value
builtins.input = _input
sys.argv = [sys.argv[1]]
runpy.run_path(sys.argv[0], run_name='__main__')
"""

def run_with_transcript(script, inputs):
    result = subprocess.run(
        [sys.executable, '-c', _ECHO_RUNNER, script, json.dumps(inputs)],
        capture_output=True, text=True, check=True,
    )
    shown = script
    return (PROMPT + 'python3 ' + shown + '\n' + result.stdout).rstrip('\n')

def run_prolog_session(script, lines):
    """Drive an interactive SWI-Prolog session in a pseudo-terminal: wait for the
    ?- (query) or |: (read/1) prompt, type the next line, and record everything
    the terminal shows, including the echoed input."""
    import re
    import pexpect
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
    if text.endswith('?-'):          # swipl can exit before the final 'halt.' is echoed
        text += ' ' + lines[-1]
    return PROMPT + 'swipl ' + script + '\n' + text

def split_code_two_columns(lines):
    # Split near the middle, preferring a blank line so a function is not cut mid-body.
    mid = len(lines) // 2
    for offset in range(0, mid):
        for idx in (mid + offset, mid - offset):
            if 0 < idx < len(lines) and not lines[idx - 1].strip():
                return lines[:idx], lines[idx:]
    return lines[:mid], lines[mid:]

def paginate_code(lines, per_page=LINES_PER_PAGE, lookback=15):
    # Break pages at a blank line close to the limit so functions are not cut mid-body.
    pages, start = [], 0
    while len(lines) - start > per_page:
        cut = start + per_page
        for idx in range(cut, cut - lookback, -1):
            if not lines[idx - 1].strip():
                cut = idx
                break
        pages.append(lines[start:cut])
        start = cut
    pages.append(lines[start:])
    return pages

def create_experiment_pdf_pages(pdf_path, code_pages, term_pages):
    """code_pages: list of (PIL image, is_two_col); term_pages: list of PIL images.
    Same layout as create_experiment_pdf, but long outputs continue on extra pages."""
    doc = fitz.open()
    tmp = 'temp_page.png'

    def add_page(label, img, is_two_col):
        page = doc.new_page(width=612, height=792)
        page.insert_image(fitz.Rect(184.875, 22.5, 427.125, 52.5), filename=HEADER_IMAGE_PATH)
        page.insert_text(fitz.Point(72.0, 80.0), label, fontname='times-bold', fontsize=12.0)
        img.save(tmp)
        w, h = img.size
        target_w = 512.0 if is_two_col else 468.0
        target_h = target_w * (h / w)
        max_h = 750.0 - 89.37
        if target_h > max_h:
            target_h = max_h
            target_w = target_h * (w / h)
        x0 = (612.0 - target_w) / 2.0 if is_two_col else 72.0
        page.insert_image(fitz.Rect(x0, 89.37, x0 + target_w, 89.37 + target_h), filename=tmp)

    for i, (img, two) in enumerate(code_pages):
        add_page('Code:' if i == 0 else 'Code (continued):', img, two)
    for i, img in enumerate(term_pages):
        add_page('Output:' if i == 0 else 'Output (continued):', img, False)

    doc.save(pdf_path, deflate=True, garbage=4, clean=True)
    doc.close()
    if os.path.exists(tmp):
        os.remove(tmp)
    print(f'Successfully created {pdf_path} ({os.path.getsize(pdf_path)} bytes)')

def build_experiment(pdf_name, script, inputs=()):
    with open(script) as f:
        code = f.read().rstrip('\n')
    lines = code.splitlines(keepends=True)
    # Long programs continue on extra single-column pages instead of being squeezed
    # into two tiny columns, so the printout stays readable.
    lexer = PrologLexer() if script.endswith('.pl') else PythonLexer()
    code_pages = [(render_code_single_column(''.join(chunk).rstrip('\n'), font_size=20, line_height=30, lexer=lexer), False)
                  for chunk in paginate_code(lines)]

    if script.endswith('.pl'):
        term = run_prolog_session(script, list(inputs))
    else:
        term = run_with_transcript(script, list(inputs))
    term_lines = term.splitlines()
    term_pages = [
        render_terminal_screenshot('\n'.join(term_lines[i:i + LINES_PER_PAGE]), font_size=20, line_height=29)
        for i in range(0, len(term_lines), LINES_PER_PAGE)
    ]
    create_experiment_pdf_pages(pdf_name, code_pages, term_pages)

# Experiment number -> (output PDF, program, scripted stdin).
# Same layout as the DAA lab files: GEC header, syntax-highlighted code, terminal output.
EXPERIMENTS = {
    9: ('exp9/exp9.pdf', 'exp9/exp9.py',
        ['1 2 3', '_ 4 6', '7 5 8',      # initial state
         '1 2 3', '4 5 6', '7 8 _']),    # goal state
    # Prolog: answers typed at the ?- and |: prompts of an interactive swipl session
    10: ('exp10/exp10_code_output.pdf', 'exp10/expert_system.pl',
         ['go.', 'yes.', 'yes.', 'yes.', 'no.', 'yes.',                    # -> tiger
          'go.', 'no.', 'no.', 'yes.', 'yes.', 'no.', 'yes.', 'yes.',      # -> penguin
          'halt.']),
    11: ('exp11/exp11_code_output.pdf', 'exp11/resolution.pl',
         ['hate(marcus, caesar).', 'roman(X).',
          'query(hate(marcus, caesar)).', 'query(hate(caesar, caesar)).', 'halt.']),
}

def main():
    """python3 generate_experiment_pdfs.py      -> build every experiment
       python3 generate_experiment_pdfs.py 9    -> build only experiment 9"""
    wanted = [int(a) for a in sys.argv[1:]] or sorted(EXPERIMENTS)
    for n in wanted:
        if n in EXPERIMENTS:
            build_experiment(*EXPERIMENTS[n])
        else:
            print(f'Experiment {n}: not configured, skipped')

if __name__ == '__main__':
    main()
