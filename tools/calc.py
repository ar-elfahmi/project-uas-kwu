"""Hitung ulang xlsx dengan lib formulas, simpan nilai ke JSON (sheet -> sel -> nilai)."""
import formulas, sys, json, re
path = sys.argv[1]
xl = formulas.ExcelModel().loads(path).finish()
sol = xl.calculate()
out = {}
for k, v in sol.items():
    m = re.match(r"'\[.*?\](.*?)'!([A-Z]+\d+)$", k)
    if not m:
        continue
    try:
        val = v.value[0, 0]
    except Exception:
        continue
    if hasattr(val, 'item'):
        val = val.item()
    out.setdefault(m.group(1), {})[m.group(2)] = val if isinstance(val, (int, float, str, bool)) else str(val)
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False)
print(len(out), 'sheets')
