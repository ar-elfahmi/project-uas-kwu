import json, sys, os
v = json.load(open(os.environ['KIROCREW_SCRATCH'] + r'\vals.json'))
def g(s, c): return v.get(s.upper(), {}).get(c)
print(list(v.keys()))
for s in sys.argv[1:]:
    sh = v.get(s.upper(), {})
    print('==', s, len(sh))
    # print by rows
    rows = {}
    for k, val in sh.items():
        import re
        m = re.match(r'([A-Z]+)(\d+)', k)
        rows.setdefault(int(m.group(2)), {})[m.group(1)] = val
    for r in sorted(rows):
        print(r, {c: (round(x, 1) if isinstance(x, float) else x) for c, x in sorted(rows[r].items(), key=lambda t: (len(t[0]), t[0]))})
