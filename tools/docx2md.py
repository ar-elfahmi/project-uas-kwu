import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
d = Document(sys.argv[1]); out = []
body = d.element.body
skip = True
for el in body.iterchildren():
    tag = el.tag.split('}')[1]
    if tag == 'p':
        p = Paragraph(el, d); t = p.text.strip(); s = p.style.name
        if not t: continue
        if s == 'Heading 1': out.append('\n## ' + t.title().replace('Dan ', 'dan ').replace('Ai', 'AI')); continue
        if s == 'Heading 2': out.append('\n### ' + t); continue
        if s.startswith('List'): out.append('- ' + t); continue
        if t.startswith(('Tabel ', 'Gambar ')) and len(t) < 160: out.append('\n*' + t + '*\n'); continue
        out.append(t + '\n')
    elif tag == 'tbl':
        tb = Table(el, d)
        rows = [[c.text.replace('\n', ' ').replace('|', '/').strip() for c in r.cells] for r in tb.rows]
        if len(rows) == 1 and len(rows[0]) == 1: out.append('> ' + rows[0][0] + '\n'); continue
        out.append('| ' + ' | '.join(rows[0]) + ' |'); out.append('|' + '---|' * len(rows[0]))
        for r in rows[1:]: out.append('| ' + ' | '.join(r) + ' |')
        out.append('')
txt = '\n'.join(out)
head = sys.argv[3] if len(sys.argv) > 3 else ''
open(sys.argv[2], 'w', encoding='utf8').write(head + txt)
print(len(txt))
