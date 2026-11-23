import openpyxl, sys
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L

N = 8  # target responden (minimal 5)
OUT = r'D:\08_CodeKuliah\project-uas-kwu\output\05_form_rekap_uji.xlsx'
if len(sys.argv) > 1: OUT = sys.argv[1]
wb = openpyxl.Workbook()
H = PatternFill('solid', fgColor='1F3A5F'); HF = Font(bold=True, color='FFFFFF')
IN = Font(color='0000FF'); YEL = PatternFill('solid', fgColor='FFF2CC')

def hdr(ws, row, vals):
    for i, v in enumerate(vals, 1):
        c = ws.cell(row=row, column=i, value=v); c.fill = H; c.font = HF; c.alignment = Alignment(wrap_text=True, vertical='center')

# ---- Petunjuk
p = wb.active; p.title = 'Petunjuk'
for i, t in enumerate([
    'REKAP UJI PENGGUNA TUMBUH.IN (Form 2 dan Form 3)',
    'Isi hanya sel biru (jawaban asli responden). Sel kosong = belum diuji. Jangan mengetik angka contoh.',
    'SUS: butir ganjil (1,3,5,7,9) kontribusi = skor - 1; butir genap (2,4,6,8,10) kontribusi = 5 - skor; jumlah x 2,5 = skor 0-100.',
    'Skala jawaban 1 (sangat tidak setuju) sampai 5 (sangat setuju). Kode responden R-U1 dst; tanpa nama.',
    'Target ditetapkan sebelum uji (sheet Ringkasan, kolom Target). Laporkan hasil apa adanya.',
    'Minimal 5 responden segmen target (kriteria UAS); target tim 8.'], 1):
    p.cell(row=i, column=1, value=t)
p['A1'].font = Font(bold=True, size=13); p.column_dimensions['A'].width = 120

# ---- Profil
pr = wb.create_sheet('Profil')
hdr(pr, 1, ['Kode', 'Jenis usaha', 'Peran (pemilik/pelayan)', 'Pengalaman aplikasi kasir/catat', 'Perangkat', 'Segmen target? (Ya/Tidak)'])
for r in range(2, 2 + N):
    pr.cell(row=r, column=1, value=f'R-U{r-1}')
    for c in range(2, 7): pr.cell(row=r, column=c).font = IN
for i, w in enumerate([8, 24, 22, 30, 14, 22], 1): pr.column_dimensions[L(i)].width = w

# ---- Tugas
tg = wb.create_sheet('Tugas')
hdr(tg, 1, ['Kode', 'T1 selesai (1/0)', 'T1 detik', 'T2 selesai (1/0)', 'T2 detik', 'T3 selesai (1/0)', 'T3 detik', 'T4 selesai (1/0)', 'T4 detik', 'Keberhasilan tugas', 'Total detik rekap (T1-T3)', 'Rekap < 10 menit tanpa bantuan? (1/0)'])
for r in range(2, 2 + N):
    tg.cell(row=r, column=1, value=f'R-U{r-1}')
    for c in range(2, 10): tg.cell(row=r, column=c).font = IN
    tg.cell(row=r, column=10, value=f'=IF(COUNT(B{r},D{r},F{r},H{r})=0,"",(B{r}+D{r}+F{r}+H{r})/4)').number_format = '0%'
    tg.cell(row=r, column=11, value=f'=IF(COUNT(C{r},E{r},G{r})<3,"",C{r}+E{r}+G{r})')
    tg.cell(row=r, column=12).font = IN
a, b = 2, 1 + N
tg.cell(row=b + 2, column=1, value='Rata-rata keberhasilan')
tg.cell(row=b + 2, column=10, value=f'=IF(COUNT(J{a}:J{b})=0,"",AVERAGE(J{a}:J{b}))').number_format = '0%'
tg.cell(row=b + 3, column=1, value='Rekap < 10 menit (jumlah)')
tg.cell(row=b + 3, column=12, value=f'=SUM(L{a}:L{b})')
for i in range(1, 13): tg.column_dimensions[L(i)].width = 15
tg.row_dimensions[1].height = 45

# ---- SUS (Form 2)
s = wb.create_sheet('SUS_Form2')
hdr(s, 1, ['Kode'] + [f'B{i}' for i in range(1, 11)] + ['Skor SUS (0-100)'])
for r in range(2, 2 + N):
    s.cell(row=r, column=1, value=f'R-U{r-1}')
    for c in range(2, 12): s.cell(row=r, column=c).font = IN
    terms = '+'.join([f'(B{r}-1)' if i % 2 == 1 else f'(5-{L(1+i)}{r})' for i in range(1, 11)])
    terms = '+'.join([f'({L(1+i)}{r}-1)' if i % 2 == 1 else f'(5-{L(1+i)}{r})' for i in range(1, 11)])
    s.cell(row=r, column=12, value=f'=IF(COUNT(B{r}:K{r})<10,"",({terms})*2.5)').number_format = '0.0'
n = 2 + N + 1
labels = [('Jumlah responden terisi', f'=COUNT(L{a}:L{b})', '0'),
          ('Rata-rata SUS', f'=IF(COUNT(L{a}:L{b})=0,"",AVERAGE(L{a}:L{b}))', '0.0'),
          ('Simpangan baku', f'=IF(COUNT(L{a}:L{b})<2,"",STDEV(L{a}:L{b}))', '0.0'),
          ('Batas bawah IK 95%', f'=IF(COUNT(L{a}:L{b})<2,"",B{n+1}-TINV(0.05,B{n}-1)*B{n+2}/SQRT(B{n}))', '0.0'),
          ('Batas atas IK 95%', f'=IF(COUNT(L{a}:L{b})<2,"",B{n+1}+TINV(0.05,B{n}-1)*B{n+2}/SQRT(B{n}))', '0.0'),
          ('Status terhadap target 68', f'=IF(B{n+1}="","Belum diuji",IF(B{n+1}>=68,"Tercapai","Belum tercapai"))', '@')]
for i, (lab, f, fmt) in enumerate(labels):
    s.cell(row=n + i, column=1, value=lab); c = s.cell(row=n + i, column=2, value=f); c.number_format = fmt
# kontribusi per butir
s.cell(row=n + 7, column=1, value='Kontribusi rata-rata per butir (0-4)').font = Font(bold=True)
for i in range(1, 11):
    col = L(1 + i)
    f = f'=IF(COUNT({col}{a}:{col}{b})=0,"",AVERAGE({col}{a}:{col}{b})-1)' if i % 2 == 1 else f'=IF(COUNT({col}{a}:{col}{b})=0,"",5-AVERAGE({col}{a}:{col}{b}))'
    s.cell(row=n + 8, column=1 + i, value=f).number_format = '0.00'
    s.cell(row=n + 7, column=1 + i, value=f'B{i}').font = Font(bold=True)
s.column_dimensions['A'].width = 38
for i in range(2, 13): s.column_dimensions[L(i)].width = 9

# ---- Validasi (Form 3)
v = wb.create_sheet('Validasi_Form3')
hdr(v, 1, ['Kode', 'C1 Membantu masalah (1-5)', 'C2 Minat memakai (1-5)', 'C3 Fitur paling berguna', 'C4 Mau bayar Rp24.000/bln? (1/0)', 'C4b Mau uang muka Rp10.000? (1/0)', 'C5 Sangat kecewa jika tak bisa pakai? (1/0)', 'C6 Saran terbuka'])
for r in range(2, 2 + N):
    v.cell(row=r, column=1, value=f'R-U{r-1}')
    for c in range(2, 9): v.cell(row=r, column=c).font = IN
n2 = 2 + N + 1
rows = [('Setuju membantu (skor 4-5)', f'=IF(COUNT(B{a}:B{b})=0,"",COUNTIF(B{a}:B{b},">=4")/COUNT(B{a}:B{b}))', '0%'),
        ('Minat memakai (skor 4-5)', f'=IF(COUNT(C{a}:C{b})=0,"",COUNTIF(C{a}:C{b},">=4")/COUNT(C{a}:C{b}))', '0%'),
        ('Mau membayar Rp24.000', f'=IF(COUNT(E{a}:E{b})=0,"",SUM(E{a}:E{b})/COUNT(E{a}:E{b}))', '0%'),
        ('Mau uang muka Rp10.000 (jumlah)', f'=SUM(F{a}:F{b})', '0'),
        ('Sangat kecewa (Sean Ellis)', f'=IF(COUNT(G{a}:G{b})=0,"",SUM(G{a}:G{b})/COUNT(G{a}:G{b}))', '0%')]
for i, (lab, f, fmt) in enumerate(rows):
    v.cell(row=n2 + i, column=1, value=lab); v.cell(row=n2 + i, column=2, value=f).number_format = fmt
v.column_dimensions['A'].width = 34
for i in range(2, 9): v.column_dimensions[L(i)].width = 20
v.row_dimensions[1].height = 45

# ---- Ringkasan
r = wb.create_sheet('Ringkasan')
hdr(r, 1, ['Indikator', 'Target (ditetapkan sebelum uji)', 'Hasil', 'Status'])
items = [('Jumlah responden segmen target', 5, f"=COUNTIF(Profil!F2:F{1+N},\"Ya\")", '>='),
         ('Keberhasilan tugas rata-rata', 0.8, f"=Tugas!J{b+2}", '>='),
         ('Skor SUS rata-rata', 68, "=SUS_Form2!B%d" % (n + 1), '>='),
         ('Setuju aplikasi membantu (4-5)', 0.7, "=Validasi_Form3!B%d" % n2, '>='),
         ('Mau uang muka Rp10.000 (A1: 6 dari 10)', 0.6, f"=IF(COUNT(Validasi_Form3!F{a}:F{b})=0,\"\",SUM(Validasi_Form3!F{a}:F{b})/COUNT(Validasi_Form3!F{a}:F{b}))", '>='),
         ('Rekap < 10 menit tanpa bantuan (A2: 7 dari 10)', 0.7, f"=IF(COUNT(Tugas!L{a}:L{b})=0,\"\",SUM(Tugas!L{a}:L{b})/COUNT(Tugas!L{a}:L{b}))", '>='),
         ('Sangat kecewa (indikatif, Sean Ellis)', 0.4, "=Validasi_Form3!B%d" % (n2 + 4), '>=')]
for i, (lab, t, f, op) in enumerate(items, 2):
    r.cell(row=i, column=1, value=lab)
    c = r.cell(row=i, column=2, value=t); c.font = IN; c.fill = YEL
    h = r.cell(row=i, column=3, value=f)
    pctfmt = isinstance(t, float) and t < 1.01
    for x in (c, h): x.number_format = '0%' if pctfmt else '0.0'
    r.cell(row=i, column=4, value=f'=IF(C{i}="","Belum diuji",IF(C{i}>=B{i},"Tercapai","Belum tercapai"))')
r.column_dimensions['A'].width = 48; r.column_dimensions['B'].width = 28; r.column_dimensions['C'].width = 14; r.column_dimensions['D'].width = 18
wb.move_sheet('Ringkasan', offset=-5)
wb.calculation.fullCalcOnLoad = True
wb.save(OUT); print('saved', OUT)
