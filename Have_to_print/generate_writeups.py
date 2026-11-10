"""Write-ups for AI lab experiments: Aim, Theory, Algorithm (+ Code/Output for Prolog).

Lab numbering is one ahead of the CMP-305 syllabus (the lab added an extra
experiment), so lab exp9 = syllabus 8, exp10 = syllabus 9, exp11 = syllabus 10.
Aim = experiment title from the syllabus. Algorithm for exp9 is transcribed from
Deepak Khemani, A First Course in Artificial Intelligence (text book 1), Figure 3.7.

Usage:  python3 generate_writeups.py            -> all write-ups
        python3 generate_writeups.py 10 11      -> only those experiments
For Prolog experiments run generate_experiment_pdfs.py first: its code/output
pages are appended after the write-up to give the complete expN/expN.pdf.
"""
import html
import os
import sys

import fitz

HEADER_IMAGE_PATH = 'assets/gec_header.png'

CSS = """
body  { font-family: Times; font-size: 12pt; line-height: 1.25; }
h1    { font-family: Times; font-size: 13pt; font-weight: bold; text-align: center; margin: 0 0 8pt 0; }
h2    { font-family: Times; font-size: 12pt; font-weight: bold; margin: 9pt 0 3pt 0; }
p     { margin: 0 0 5pt 0; text-align: justify; }
li    { margin: 0 0 2pt 0; text-align: justify; }
pre   { font-family: Courier; font-size: 9.8pt; line-height: 1.25; margin: 2pt 0 5pt 6pt; }
.cap  { text-align: center; font-size: 10pt; font-style: italic; margin: 0 0 6pt 0; }
.note { font-size: 10pt; font-style: italic; }
"""


def esc(s):
    return html.escape(s, quote=False)


def render_pdf(pdf_path, body_html, append_pdf=None):
    """Lay the HTML out on Letter pages and stamp the GEC header on every page.
    If append_pdf is given, its pages (code + output) are added at the end."""
    story = fitz.Story(html='<body>' + body_html + '</body>', user_css=CSS)
    tmp = pdf_path + '.tmp'
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
    if append_pdf:
        doc.insert_pdf(fitz.open(append_pdf))
    doc.save(pdf_path, deflate=True, garbage=4)
    doc.close()
    os.remove(tmp)
    print(f'Successfully created {pdf_path} ({os.path.getsize(pdf_path)} bytes)')


# ---------------------------------------------------------------------------
# Experiment 9 (syllabus 8): Eight puzzle, Hill Climbing
# ---------------------------------------------------------------------------
def exp9_html():
    return f"""
<h1>Experiment 9: Eight Puzzle using Hill Climbing</h1>
<h2>Aim:</h2>
<p>Program to implement a Game Playing algorithm for eight puzzle program/ Graph.</p>

<h2>Theory:</h2>
<p>The <b>8-puzzle</b> is a 3 × 3 board with eight numbered tiles and one blank square. A tile next to the blank can
slide into it. Equivalently, the blank moves Up, Down, Left or Right, so each state has two to four successors
depending on where the blank is. Given a start state and a goal state, the task is to find a sequence of moves that
transforms one into the other. From any state, 9!/2 = 181,440 states are reachable, so blind search is wasteful and
the problem is a standard example of <b>heuristic search</b>.</p>
<p><b>Heuristic function.</b> A heuristic function h(n) estimates how far a state n is from the goal, and h(goal) = 0.
Two common heuristics for the 8-puzzle are:</p>
<ul>
<li><b>h<sub>1</sub>(n)</b>: the number of tiles out of place (Hamming distance). The blank is not counted.</li>
<li><b>h<sub>2</sub>(n)</b>: the sum, over all tiles, of the Manhattan distance of each tile from its goal position.</li>
</ul>
<p>The program uses h<sub>1</sub>, and for every state it also prints which tiles are misplaced.</p>
<p><b>Hill Climbing.</b> Hill climbing is a local search algorithm that uses only the heuristic value to decide its
next move. From the current node it generates all successors with <i>MoveGen</i>, sorts them on h, and moves to the
best successor, but only if that successor is better than the current node (for the 8-puzzle, a lower h). It keeps no
OPEN or CLOSED list and never backtracks, so it needs only <b>constant space</b>, and its time is proportional to the
number of moves made. Because it always moves in the direction of greatest improvement, this form is also called
<b>steepest gradient ascent</b> (or descent, when h is being minimised). The search has turned from finding a goal
node into optimising the value of h.</p>
<p>The algorithm stops when no successor is better than the current node. If that node is the goal, the search has
succeeded. Otherwise it is stuck in one of these situations:</p>
<ul>
<li><b>Local optimum:</b> every neighbour is worse, although the goal lies elsewhere.</li>
<li><b>Plateau:</b> neighbours have the same heuristic value, so there is no gradient to follow.</li>
<li><b>Ridge:</b> the better states lie in a direction that no single move can reach.</li>
</ul>
<p>Hill climbing is therefore <b>not complete</b>: even for a solvable puzzle, h<sub>1</sub> may lead it to a local
minimum. Its strengths are speed and very low memory use. Variations such as random restarts, stochastic hill climbing,
simulated annealing and tabu search exist to escape local optima. For each step the program prints every neighbour with
its misplaced tiles and h(n), the chosen move, and finally whether the goal was reached or the search stopped at a local
minimum or plateau.</p>

<h2>Algorithm:</h2>
<p class="note">Deepak Khemani, A First Course in Artificial Intelligence, Figure 3.7.</p>
<pre>{esc('''HillClimbing()
1  node ← start
2  newNode ← Head(Sortₕ(MoveGen(node)))
3  while h(newNode) < h(node)
4     do node ← newNode
5        newNode ← Head(Sortₕ(MoveGen(node)))
6  return newNode''')}</pre>
<p class="cap">Figure 3.7 Algorithm Hill Climbing</p>
<p class="note">MoveGen(node) returns the successors of node (blank moved Up/Down/Left/Right), Sortₕ orders them by
increasing h, and Head picks the first, i.e. the best, successor.</p>
"""


# ---------------------------------------------------------------------------
# Experiment 10 (syllabus 9): Expert system in Prolog
# ---------------------------------------------------------------------------
def exp10_html():
    return """
<h1>Experiment 10: Expert System using Prolog</h1>
<h2>Aim:</h2>
<p>Program to develop an Expert System using Prolog.</p>

<h2>Theory:</h2>
<p>An <b>expert system</b> is a program that captures the knowledge of a human expert in a narrow domain and uses it
to solve problems or give advice in that domain, for example medical diagnosis, fault finding or classification. Its
main components are:</p>
<ul>
<li><b>Knowledge base</b>: domain knowledge stored as facts and IF–THEN rules.</li>
<li><b>Inference engine</b>: applies the rules to the known facts to reach conclusions, by forward chaining
(data driven) or backward chaining (goal driven).</li>
<li><b>Working memory</b>: the facts known about the current case, such as the user's answers.</li>
<li><b>User interface</b>: asks the user questions and presents the conclusion.</li>
<li><b>Explanation facility</b> (optional): shows how a conclusion was reached.</li>
</ul>
<p><b>Why Prolog.</b> Prolog (PROgramming in LOGic) is a declarative language built from three elements: <b>facts</b>
(relations that are unconditionally true), <b>rules</b> (relations that are true when their conditions hold) and
<b>queries</b> (questions answered from the facts and rules). These map directly onto an expert system. The rule</p>
<pre>tiger :- mammal, carnivore, verify(has_tawny_color), verify(has_black_stripes).</pre>
<p>reads "the animal is a tiger IF it is a mammal AND a carnivore AND has a tawny colour AND has black stripes". To
answer a query, Prolog uses goal-driven <b>backward chaining</b> with depth-first search and backtracking, so
Prolog itself is the inference engine and no separate engine has to be written.</p>
<p><b>Working of the program (animal identification).</b></p>
<ul>
<li>The query <i>go</i> starts a consultation. <i>hypothesize/1</i> tries each hypothesis in order: cheetah, tiger,
giraffe, zebra, ostrich, penguin, albatross. The cut (!) stops at the first hypothesis that can be proved, and if
none can, the answer is <i>unknown</i>.</li>
<li>Each hypothesis is proved through intermediate classification rules (<i>mammal, bird, carnivore, ungulate</i>),
which depend on observable attributes checked with <i>verify/1</i>.</li>
<li><i>verify/1</i> first looks in working memory, the dynamic predicates <i>yes/1</i> and <i>no/1</i>. Only if the
attribute is unknown does <i>ask/1</i> put the question to the user. The answer is stored with <i>assertz/1</i>, so
no question is asked twice in a consultation, even when several rules need the same attribute.</li>
<li><i>undo/0</i> retracts all yes/no facts at the end, so the next consultation starts with empty working memory.</li>
</ul>
<p><b>Sample consultations.</b> In the first run the animal has hair, eats meat and has a tawny colour but no dark
spots, so <i>cheetah</i> fails. Prolog backtracks to <i>tiger</i>, reuses the stored answers, asks only about black
stripes, and concludes <b>tiger</b>. In the second run the animal has no hair and gives no milk, so every mammal
hypothesis fails. It has feathers and does not fly, but its neck is not long (so not an ostrich), and it swims and
is black and white, so the system concludes <b>penguin</b>.</p>
"""


# ---------------------------------------------------------------------------
# Experiment 11 (syllabus 10): Resolution in Prolog
# ---------------------------------------------------------------------------
def exp11_html():
    return """
<h1>Experiment 11: Logical Inference using Resolution in Prolog</h1>
<h2>Aim:</h2>
<p>Program to perform logical inference using Resolution in Prolog.</p>

<h2>Theory:</h2>
<p><b>Resolution</b> is a single, sound rule of inference for propositional and first-order logic. Given two clauses
where one contains a literal L and the other its negation ¬L, resolution produces a new clause, the
<b>resolvent</b>, made of the remaining literals of both: from (A ∨ L) and (B ∨ ¬L) infer (A ∨ B). In first-order
logic the two literals only need to <b>unify</b>. The most general unifier is found and applied to the resolvent.</p>
<p><b>Resolution refutation.</b> To prove a statement P from a knowledge base:</p>
<ol>
<li>Convert every statement to clause form (conjunctive normal form): eliminate implications, move negations
inwards, standardise variables, Skolemise existential quantifiers, drop universal quantifiers, and split the
conjunctions into separate clauses.</li>
<li>Negate P, convert it to clause form and add it to the set of clauses.</li>
<li>Repeatedly pick two clauses with complementary literals, resolve them, and add the resolvent to the set.</li>
<li>If the empty clause [ ] is derived, there is a contradiction: ¬P is inconsistent with the knowledge base, so
P is true. If no new resolvent can be produced, P cannot be proved.</li>
</ol>
<p><b>Resolution in Prolog.</b> Prolog is built on <b>SLD resolution</b>, a restricted and efficient form of
resolution for <b>Horn clauses</b> (clauses with at most one positive literal). The rule
hate(X, caesar) :- roman(X), notloyalto(X, caesar) is the clause hate(X, caesar) ∨ ¬roman(X) ∨
¬notloyalto(X, caesar), and a fact is a clause with a single positive literal. A query ?- G. adds the negated goal
¬G. Prolog then resolves the leftmost literal of the current goal clause with the first program clause whose head
unifies with it, working top to bottom and depth first, and backtracks on failure. An empty goal is the empty
clause: Prolog answers <i>true</i> and reports the variable bindings, exactly as in the recursion example
is_digesting(lion, grass) traced in class.</p>
<p><b>Knowledge base used (Marcus example):</b></p>
<ol>
<li>Marcus was a man: man(marcus).</li>
<li>Marcus was a Pompeian: pompeian(marcus).</li>
<li>All Pompeians were Romans: roman(X) :- pompeian(X).</li>
<li>Caesar was a ruler: ruler(caesar).</li>
<li>Every man is a person: person(X) :- man(X).</li>
<li>People who try to assassinate a ruler are not loyal to him:
notloyalto(X, Y) :- person(X), ruler(Y), tryassassinate(X, Y).</li>
<li>Marcus tried to assassinate Caesar: tryassassinate(marcus, caesar).</li>
<li>A Roman who is not loyal to Caesar hates him: hate(X, caesar) :- roman(X), notloyalto(X, caesar).</li>
</ol>
<p>To prove hate(marcus, caesar), the predicate <i>refute/1</i> adds ¬hate(marcus, caesar). It resolves that with
clause 8 (X = marcus), then with clauses 3, 2, 6, 5, 1, 4 and 7, and derives the empty clause in 8 steps, printing
the literal resolved, the clause used and the new resolvent at every step. For hate(caesar, caesar), the literal
¬pompeian(caesar) matches no clause, so no refutation exists and the query cannot be proved.</p>
"""


# lab exp -> (final PDF, write-up builder, code/output PDF to append or None)
WRITEUPS = {
    9: ('exp9/exp9_writeup.pdf', exp9_html, None),
    10: ('exp10/exp10.pdf', exp10_html, 'exp10/exp10_code_output.pdf'),
    11: ('exp11/exp11.pdf', exp11_html, 'exp11/exp11_code_output.pdf'),
}


def main():
    wanted = [int(a) for a in sys.argv[1:]] or sorted(WRITEUPS)
    for n in wanted:
        out, build, append = WRITEUPS[n]
        render_pdf(out, build(), append)


if __name__ == '__main__':
    main()
