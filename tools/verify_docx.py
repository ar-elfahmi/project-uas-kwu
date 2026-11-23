import sys, re
from docx import Document
d = Document(sys.argv[1])
txt = [p.text for p in d.paragraphs]
for t in d.tables:
    for r in t.rows:
        for c in r.cells:
            txt.append(c.text)
full = '\n'.join(txt)
print('paragraphs', len(d.paragraphs), 'tables', len(d.tables), 'images', len(d.inline_shapes), 'words', len(full.split()))
for pat in ['StokMudah', 'Tim 3', '149.000', r'\[ISI', r'\[BELUM', 'nan', 'None', r'\{', 'TODO', '9.550']:
    m = [x for x in re.finditer(pat, full)]
    if m:
        print('FOUND', pat, len(m), full[max(0, m[0].start() - 60):m[0].end() + 60].replace('\n', ' | '))
heads = [p.text for p in d.paragraphs if p.style.name.startswith('Heading')]
print(heads)
if len(sys.argv) > 2:
    print(full[:int(sys.argv[2])])
