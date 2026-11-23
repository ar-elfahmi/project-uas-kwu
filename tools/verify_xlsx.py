import openpyxl, re
T = openpyxl.load_workbook(r'D:\08_CodeKuliah\project-uas-kwu\Salinan dari Format_Laporan_Keuangan_Proyek_Usaha_Digital.xlsx')
O = openpyxl.load_workbook(r'D:\08_CodeKuliah\project-uas-kwu\output\Lampiran_Keuangan_Tumbuh-in.xlsx')
bad = 0
for ws in T:
    wo = O[ws.title]
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and c.value.startswith('='):
                if wo[c.coordinate].value != c.value:
                    print('FORMULA CHANGED', ws.title, c.coordinate, c.value, wo[c.coordinate].value); bad += 1
pat = re.compile(r'StokMudah|Tim 3|149\.?000|angel|rekaan|freelancer', re.I)
for ws in O:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and pat.search(c.value):
                print('LEFTOVER', ws.title, c.coordinate, c.value[:100]); bad += 1
a = O['Asumsi']
for r in range(5, 43):
    if isinstance(a['B%d' % r].value, (int, float)) and r not in range(32, 34) and not a['D%d' % r].value and r < 32:
        print('NO SOURCE', r, a['A%d' % r].value); bad += 1
print('issues:', bad)
