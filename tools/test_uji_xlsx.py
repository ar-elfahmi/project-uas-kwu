"""Uji rumus dengan data DUMMY pada salinan di scratch. File hasil tidak masuk output."""
import os, subprocess, sys, json, openpyxl, statistics, math
sc = os.environ['KIROCREW_SCRATCH']
t = sc + r'\uji_test.xlsx'
subprocess.run([sys.executable, r'D:\08_CodeKuliah\project-uas-kwu\tools\build_uji_xlsx.py', t], check=True)
wb = openpyxl.load_workbook(t)
sus = [[4, 2, 4, 1, 5, 2, 4, 2, 4, 1], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]]
for i, row in enumerate(sus):
    for j, x in enumerate(row): wb['SUS_Form2'].cell(row=2 + i, column=2 + j, value=x)
for i in range(3):
    wb['Validasi_Form3'].cell(row=2 + i, column=2, value=[5, 4, 2][i]); wb['Validasi_Form3'].cell(row=2 + i, column=6, value=[1, 1, 0][i])
    wb['Profil'].cell(row=2 + i, column=6, value='Ya')
wb.save(t)
subprocess.run([sys.executable, r'D:\08_CodeKuliah\project-uas-kwu\tools\calc.py', t, sc + r'\uji_vals.json'], check=True, capture_output=True)
v = json.load(open(sc + r'\uji_vals.json'))
def sc_(r):
    return sum((x - 1) if (i % 2 == 0) else (5 - x) for i, x in enumerate(r)) * 2.5
exp = [sc_(r) for r in sus]
got = [v['SUS_FORM2'].get('L%d' % (2 + i)) for i in range(3)]
print('expected', exp, 'got', got)
print('mean', v['SUS_FORM2'].get('B12'), statistics.mean(exp))
print({k: x for k, x in v['SUS_FORM2'].items() if k.startswith('B1') and len(k) == 3})
print({k: x for k, x in v['RINGKASAN'].items() if k[0] in 'CD'})
