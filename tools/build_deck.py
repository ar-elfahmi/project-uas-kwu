from common import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

pdfmetrics.registerFont(TTFont('A', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('AB', r'C:\Windows\Fonts\arialbd.ttf'))
pdfmetrics.registerFont(TTFont('AI', r'C:\Windows\Fonts\ariali.ttf'))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('A', normal='A', bold='AB', italic='AI', boldItalic='AB')

W, H = 960, 540
C = make_charts()
NAVY_ = colors.HexColor('#1F3A5F'); GREEN_ = colors.HexColor('#2E8B57'); ORG = colors.HexColor('#E8892B')
SOFT = colors.HexColor('#F3F6FA'); GREYC = colors.HexColor('#6B7280'); LGREEN = colors.HexColor('#E6F4EC'); LORG = colors.HexColor('#FDEFE0')
cv = canvas.Canvas(OUT + r'\Pitch_Deck_Tumbuh-in.pdf', pagesize=(W, H))
cv.setTitle('Pitch Deck Tumbuh.in - UAS Kewirausahaan Bidang TI'); cv.setAuthor('Kelompok 1')
state = {'n': 0}
TOTAL_MAIN = 15


def st(size=13, color=colors.black, bold=False, lead=None, align=0):
    return ParagraphStyle('x', fontName='AB' if bold else 'A', fontSize=size, leading=lead or size * 1.25, textColor=color, alignment=align)


def para(text, x, y_top, w, size=13, color=colors.black, bold=False, align=0, lead=None):
    p = Paragraph(text, st(size, color, bold, lead, align))
    _, h = p.wrapOn(cv, w, 1000)
    p.drawOn(cv, x, y_top - h)
    return h


def card(x, y_top, w, h, fill=SOFT, stroke=None):
    cv.setFillColor(fill)
    if stroke: cv.setStrokeColor(stroke); cv.setLineWidth(1.2)
    cv.roundRect(x, y_top - h, w, h, 8, fill=1, stroke=1 if stroke else 0)


def new(title, sub=None, section=None, lamp=False):
    if state['n'] or state.get('lamp'): cv.showPage()
    state['lamp'] = lamp or state.get('lamp')
    state['n'] += 1
    cv.setFillColor(colors.white); cv.rect(0, 0, W, H, fill=1, stroke=0)
    cv.setFillColor(NAVY_); cv.rect(0, H - 6, W, 6, fill=1, stroke=0)
    para(title, 40, H - 22, 725, 21, NAVY_, True)
    if sub: para(sub, 40, H - 52, 860, 11.5, GREYC)
    cv.setFillColor(GREYC); cv.setFont('A', 9)
    cv.drawString(40, 16, 'Tumbuh.in  |  Kelompok 1  |  UAS Kewirausahaan Bidang TI 2026/2027')
    cv.drawRightString(W - 40, 16, ('Lampiran ' if lamp else '') + str(state['n']) + ('' if lamp else f' / {TOTAL_MAIN}'))
    if section:
        cv.setFillColor(ORG); cv.roundRect(W - 190, H - 38, 150, 20, 10, fill=1, stroke=0)
        cv.setFillColor(colors.white); cv.setFont('AB', 9); cv.drawCentredString(W - 115, H - 32, section)


def tbl(data, x, y_top, widths, size=10, header=True, rowh=None):
    rows = [[Paragraph(str(c), st(size, colors.white if (header and i == 0) else colors.black, header and i == 0)) for c in r] for i, r in enumerate(data)]
    t = Table(rows, colWidths=widths)
    sty = [('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
           ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    if header: sty += [('BACKGROUND', (0, 0), (-1, 0), NAVY_)]
    sty += [('ROWBACKGROUNDS', (0, 1 if header else 0), (-1, -1), [colors.white, SOFT])]
    t.setStyle(TableStyle(sty))
    w, h = t.wrapOn(cv, sum(widths), 1000)
    t.drawOn(cv, x, y_top - h)
    return h


def img(path, x, y_top, w=None, h=None):
    ir = ImageReader(path); iw, ih = ir.getSize()
    if w and not h: h = w * ih / iw
    if h and not w: w = h * iw / ih
    cv.drawImage(path, x, y_top - h, w, h, mask='auto')
    return w, h


def stat(x, y_top, w, big, small, color=GREEN_, fill=LGREEN):
    card(x, y_top, w, 86, fill)
    para(big, x + 8, y_top - 10, w - 16, 28, color, True, 1)
    para(small, x + 8, y_top - 46, w - 16, 10.5, colors.black, False, 1)


def bullets(items, x, y_top, w, size=13, gap=6, color=colors.black):
    y = y_top
    for it in items:
        h = para('•&nbsp;&nbsp;' + it, x, y, w, size, color); y -= h + gap
    return y_top - y


# ===== 1 Cover
state['n'] = 1
cv.setFillColor(NAVY_); cv.rect(0, 0, W, H, fill=1, stroke=0)
cv.setFillColor(ORG); cv.rect(0, 0, 14, H, fill=1, stroke=0)
img(IMG + r'\uts_image1.png', 60, H - 50, h=90)
para('Tumbuh.in', 60, 380, 800, 54, colors.white, True)
para('Rekap harian dan penanda stok untuk warung makan kecil di sekitar kampus', 60, 312, 760, 22, colors.white)
para('Pitch Deck UAS: Kewirausahaan Bidang TI (FVK25612002)<br/>Kelompok 1, D4 Teknik Informatika, Fakultas Vokasi, Universitas Airlangga<br/>Dosen: Nambi Sembilu, S.Kom., M.Kom.  |  Gasal 2026/2027', 60, 240, 800, 13, colors.HexColor('#CBD5E1'), lead=19)
para('Alung Destantio C. U. P. (434241001)  ·  Daffa Eka Sujianto (434241004)  ·  Muhammad Javier Rakha Abhista (434241021)<br/>Nabil Hakim Alfikri (434241055)  ·  Alfiyan Rasyid El-Fahmi (434241047)  ·  Muhammad Reyhan Ammar (434241061)', 60, 150, 840, 11, colors.white, lead=17)

# ===== 2 Masalah
new('Rekap 60-90 menit tiap malam, atau laba tidak diketahui', '1. Masalah (hasil customer discovery, 4 wawancara, 13 Oktober 2026)', 'MASALAH')
stat(40, 450, 270, '60-90 menit', 'rekap per hari (R-02 ±60, R-04 ±90)')
stat(345, 450, 270, '2 dari 4', 'tidak mencatat; laba ditebak (R-01, R-03)', ORG, LORG)
stat(650, 450, 270, '3 dari 4', 'pernah kehabisan menu atau bahan sebelum tutup')
card(40, 345, 880, 150, SOFT)
para('<b>"Gak ate dicatet wes. Gak ate dicatet, apa dicatet."</b> R-01, menit 00:54', 60, 330, 840, 14, NAVY_)
para('<b>"Wis... satu jam lah."</b> R-02, menit 14:15 (menotal catatan tunai setelah tutup)', 60, 298, 840, 14, NAVY_)
para('<b>"Soalnya kita tidak bisa melihat barang menu yang stoknya tinggal berapa..."</b> R-04, menit 02:44', 60, 266, 840, 14, NAVY_)
para('<b>Pernyataan masalah:</b> pemilik warung makan dan kedai kecil di sekitar kampus menghitung uang dari buku atau perkiraan setiap malam tanpa catatan tersusun, dan saat jualan tidak tahu menu atau bahan yang hampir habis.', 40, 180, 880, 13.5, colors.black)
para('Sumber: Laporan UTS Kelompok 1, Bab 1. Tanda F (fakta wawancara). Responden dirujuk dengan kode.', 40, 100, 880, 10, GREYC)

# ===== 3 Bukti
new('Empat wawancara, satu pola; bukti masih tahap awal', '1. Bukti validasi: apa yang sudah dan belum terbukti', 'MASALAH')
tbl([['Kode', 'Usaha', 'Lokasi', 'Cara mencatat sekarang'],
     ['R-01', 'Warung makan dan minuman', 'SWK Srikana', 'Tidak dicatat; laba dari sisa saldo QRIS'],
     ['R-02', 'Kedai makan, pengurus paguyuban', 'SWK Srikana', 'Buku tunai + mutasi bank; rekap ±1 jam tiap malam'],
     ['R-03', 'Stand makanan', 'SWK Srikana', 'Tidak dicatat; hitung global saat tutup'],
     ['R-04', 'Warung kopi malam', 'Dekat kos', 'Buku tulis 1-1,5 jam; POS dicoba lalu ditinggalkan']],
    40, 470, [55, 190, 90, 245], 10.5)
img(IMG + r'\uts_image2.png', 640, 470, w=290)
card(40, 300, 580, 110, LGREEN)
para('<b>Sudah terbukti (F)</b>', 55, 288, 550, 13, GREEN_)
bullets(['Hambatan rekap atau laba: 4 dari 4', 'Pernah kehabisan: 3 dari 4', 'Alat lama gagal: R-04 meninggalkan POS'], 55, 266, 550, 12, 3)
card(40, 180, 580, 105, LORG)
para('<b>Belum terbukti (A)</b>', 55, 170, 550, 13, ORG)
bullets(['Kesediaan membayar (A1)', 'Rekap < 10 menit dan akurasi baca AI (A2)', 'Paguyuban membuka akses ke pedagang lain (A3)'], 55, 148, 550, 12, 3)
para('Segmen awal: 25 pedagang SWK Srikana (S: SIPUMKM Surabaya). Batas atas 58 hanya untuk uji titik impas.', 40, 40, 880, 10, GREYC)

# ===== 4 Solusi
new('Cukup catat sekali: foto nota atau satu suara', '2. Solusi dan value proposition', 'SOLUSI')
card(40, 460, 880, 78, NAVY_)
para('Untuk pemilik warung makan dan kedai kecil yang tiap malam merekap 60-90 menit atau tidak tahu laba, Tumbuh.in memberi rekap harian tunai dan QRIS dari foto nota atau satu rekaman suara, plus penanda stok. Target rekap < 10 menit (asumsi).', 55, 452, 850, 13, colors.white)
for i, (t, s, c, f) in enumerate([('H1 Rekap', 'Foto nota atau suara menjadi rekap harian; pemilik mengoreksi hasil', GREEN_, LGREEN), ('H2 Stok', 'Penanda menu atau bahan yang hampir habis', ORG, LORG), ('H3 Mudah', 'Satu layar; tidak ada input per pesanan seperti POS lama', NAVY_, SOFT)]):
    x = 40 + i * 300
    card(x, 360, 280, 130, f)
    para(t, x + 14, 348, 250, 18, c, True); para(s, x + 14, 318, 250, 12.5)
bullets(['<b>Tidak dilayani sekarang:</b> H4 makanan terbuang, H5 rekonsiliasi QRIS (cadangan)', '<b>Fitur lanjutan:</b> perkiraan belanja besok, setelah ada data catatan (2 dari 4 responden belum mencatat)', '<b>Pembeda:</b> cukup mencatat sekali saat senggang; tidak memperlambat penjualan saat ramai (R-04)'], 40, 215, 880, 13, 7)

# ===== 5 Demo
new('Demo prototipe: empat layar, alur utama 3 sampai 4 menit', '3. Prototipe (Figma klik-tembus, data contoh, tanpa AI sungguhan)', 'DEMO')
labels = [('1. Ambil nota', ['Tombol foto nota', 'Tombol rekam suara', '"Mulai dari satu nota"']), ('2. Periksa hasil', ['Es teh x 12  18.000', 'Nasi ayam x 9  135.000', 'Pemilik bisa memperbaiki']),
          ('3. Rekap harian', ['Tunai   Rp (contoh)', 'QRIS   Rp (contoh)', 'Laba hari ini  |  waktu proses']), ('4. Stok menipis', ['Ayam: sisa sedikit', 'Es batu: sisa sedikit', 'Belanja besok (lanjutan)'])]
for i, (t, ls) in enumerate(labels):
    x = 50 + i * 220
    card(x, 470, 190, 290, colors.HexColor('#111827'))
    card(x + 8, 462, 174, 274, colors.white)
    cv.setFillColor(GREEN_); cv.roundRect(x + 8, 462 - 36, 174, 36, 0, fill=1, stroke=0)
    para(t, x + 14, 456, 160, 13, colors.white, True)
    yy = 410
    for l in ls:
        card(x + 18, yy, 154, 44, SOFT); para(l, x + 24, yy - 6, 144, 10.5, colors.black); yy -= 56
    para('(data contoh)', x + 20, 245, 150, 8.5, GREYC)
para('<b>Tautan prototipe:</b> [ISI: tautan Figma yang dibuat tim]', 50, 160, 860, 14, ORG)
bullets(['Skrip demo: ambil foto nota → periksa dan koreksi satu angka → lihat rekap → lihat stok menipis', 'Layar di atas adalah sketsa untuk deck; prototipe sebenarnya dibangun di Figma oleh tim'], 50, 130, 860, 11.5, 4)

# ===== 6 Uji
new('Hasil uji pengguna: target ditetapkan sebelum uji', '3. Hasil uji pengguna (SUS + kuesioner validasi), minimal 5 responden segmen target', 'DEMO')
tbl([['Indikator', 'Target (A)', 'Hasil'],
     ['Responden segmen target', '≥ 5 (target 8)', '[BELUM DIUJI]'],
     ['Keberhasilan tugas (4 tugas)', '≥ 80%', '[BELUM DIUJI]'],
     ['Skor SUS rata-rata', '≥ 68', '[BELUM DIUJI]'],
     ['Setuju aplikasi membantu (skor 4-5)', '≥ 70%', '[BELUM DIUJI]'],
     ['Bersedia membayar Rp24.000/bulan', '≥ 6 dari 10 (A1)', '[BELUM DIUJI]'],
     ['Rekap < 10 menit tanpa bantuan', '≥ 7 dari 10 (A2)', '[BELUM DIUJI]']],
    40, 470, [260, 150, 130], 11)
card(620, 470, 300, 250, SOFT)
para('<b>4 tugas uji</b>', 635, 458, 270, 13, NAVY_)
bullets(['Ambil foto nota atau rekam suara', 'Periksa dan koreksi satu hasil', 'Baca rekap, sebut laba hari itu', 'Temukan menu yang hampir habis'], 635, 432, 275, 12, 5)
para('Responden mencoba dulu, baru mengisi kuesioner. Persetujuan lisan; kode R-U1 dst; tanpa data pribadi (UU 27/2022).', 635, 260, 275, 10.5, GREYC)
para('Hasil sengaja kosong sampai uji lapangan selesai. Tim mengisi dengan data nyata dan melaporkan apa adanya, termasuk yang tidak mencapai target.', 40, 190, 560, 13, ORG)
para('Format laporan: Format_Laporan_Hasil_Pengujian (Bab 1-8, Form 1-3).', 40, 100, 560, 10, GREYC)

# ===== 7 Model bisnis
new('Model bisnis: sembilan blok, tanda F / S / A', '4. Model bisnis (Business Model Canvas, UTS dengan koreksi UAS)', 'MODEL BISNIS')
blk = [('Segmen', 'Pemilik warung makan sekitar kampus; A sudah mencatat, B belum. Bayar: pemilik (A)'), ('Value proposition', 'Rekap tanpa menulis ulang, penanda stok, mudah, rekap < 10 menit (A)'),
       ('Kanal', 'Kunjungan, paguyuban, demo nota sendiri, web tanpa instal, WhatsApp (A)'), ('Hubungan', 'Pendampingan hari pertama, lalu swalayan; bantuan WhatsApp (A)'),
       ('Pendapatan', 'Langganan Rp24.000/bln (A); cadangan Rp1.000/rekap'), ('Sumber daya', 'Model AI (API), aplikasi web, tim, 4 responden bersedia dihubungi (F)'),
       ('Aktivitas', 'Uji akurasi baca, pendampingan, kunjungan lapangan'), ('Kemitraan', 'Penyedia AI/hosting, paguyuban, warung pilot, penyedia QRIS'),
       ('Biaya', f'Tetap {rp(FIX_H)} (hemat) / {rp(FIX_P)} (penuh); variabel {rp(VAR)}; CAC Rp30.000')]
for i, (t, s) in enumerate(blk):
    col, row = i % 3, i // 3
    x = 40 + col * 300; y = 468 - row * 130
    card(x, y, 285, 118, [LGREEN, LORG, SOFT][(col + row) % 3])
    para(t, x + 10, y - 8, 265, 13, NAVY_, True); para(s, x + 10, y - 30, 265, 11)
para('Dari 33 isian UTS: 7 F, 4 S, 22 A. Freemium gugur (tiap catatan memanggil AI).', 40, 66, 880, 10.5, GREYC)

# ===== 8 Operasional
new('Operasional: pendampingan dulu, lalu pakai mandiri', '4. Rencana operasional', 'MODEL BISNIS')
steps = [('1 Kenalan', 'Paguyuban atau kunjungan; demo dengan nota sendiri'), ('2 Pendampingan', 'Hari pertama, transport Rp30.000'), ('3 Pakai harian', 'Foto atau suara saat senggang; koreksi'),
         ('4 Bantuan', 'WhatsApp'), ('5 Tagihan', 'QRIS bulanan'), ('6 Evaluasi', 'Akurasi, churn; ekspor data mingguan')]
for i, (t, s) in enumerate(steps):
    x = 40 + i * 148
    card(x, 470, 138, 110, GREEN_ if i % 2 == 0 else NAVY_)
    para(t, x + 8, 462, 122, 12.5, colors.white, True); para(s, x + 8, 438, 122, 10.5, colors.white)
card(40, 330, 430, 190, SOFT)
para('<b>Teknologi</b>', 54, 318, 400, 13, NAVY_)
bullets(['Web responsif, Cloudflare Pages (gratis)', 'Supabase (gratis; Pro bila data > 400 MB)', 'Gemini 3.5 Flash-Lite via API', 'Foto dan suara tidak disimpan; hanya teks hasil'], 54, 295, 410, 11.5, 3)
card(490, 330, 430, 190, SOFT)
para('<b>Tim (6 anggota)</b>', 504, 318, 400, 13, NAVY_)
bullets(['Pimpinan proyek, produk dan prototipe, teknologi', 'Lapangan, pemasaran, keuangan', 'Peran per nama diisi tim'], 504, 295, 410, 11.5, 3)
para(f'<b>Pemicu tahap penuh ({rp(FIX_P)}/bln):</b> warung berbayar mendekati {BEP_P} atau basis data > 400 MB. Sebelum itu tahap hemat ({rp(FIX_H)}/bln) dengan ekspor data mingguan.', 40, 108, 880, 12.5)

# ===== 9 STP
new('Target awal: warung SWK Srikana yang sudah mencatat', '5. Strategi pemasaran: segmentasi, target, positioning', 'PEMASARAN')
card(40, 470, 280, 220, SOFT); card(340, 470, 280, 220, LGREEN); card(640, 470, 280, 220, LORG)
para('<b>Segmentasi</b>', 54, 458, 250, 15, NAVY_)
bullets(['A: sudah mencatat 60-90 menit (R-02, R-04)', 'B: belum mencatat, laba ditebak (R-01, R-03)'], 54, 428, 255, 12, 4)
para('<b>Target</b>', 354, 458, 250, 15, GREEN_)
bullets(['A dulu: workaround kuat, pengguna awal', 'SWK Srikana: 25 pedagang (S)', 'Lalu B, lalu SWK lain'], 354, 428, 255, 12, 4)
para('<b>Positioning</b>', 654, 458, 250, 15, ORG)
para('Pencatat harian untuk warung makan yang cukup dipakai sekali dari foto nota atau suara, dengan pendampingan hari pertama.', 654, 428, 255, 12)
card(40, 225, 880, 85, NAVY_)
para('<b>Positioning statement.</b> Bagi pemilik warung makan kecil yang lelah merekap tiap malam, Tumbuh.in adalah pencatat harian yang cukup dipakai sekali dari foto nota atau suara. Tidak seperti aplikasi kasir yang menuntut input tiap pesanan, Tumbuh.in tidak memperlambat penjualan saat ramai.', 55, 215, 850, 12.5, colors.white)
para('Pengguna awal bukan wakil seluruh pasar; penerimaan lebih luas belum terbukti.', 40, 120, 880, 11, GREYC)

# ===== 10 7P + harga + pesaing
new('7P, harga, dan pesaing', '5. Bauran pemasaran dan peta pesaing (diakses 23 Nov 2026)', 'PEMASARAN')
tbl([['P', 'Penerapan'], ['Product', 'Rekap dari foto/suara, penanda stok, koreksi pemilik'], ['Price', 'Rp24.000/bln; uji Rp19.000 & Rp29.000; uang muka Rp10.000'],
     ['Place', 'Web tanpa instal; kunjungan dan paguyuban'], ['Promotion', 'Demo nota sendiri, WhatsApp, Reels/TikTok demo'], ['People', 'Tim lapangan, bantuan WhatsApp'],
     ['Process', 'Kenalan → pendampingan → pakai → tagihan'], ['Physical evidence', 'Prototipe, tangkapan layar rekap, kutipan (kode)']], 40, 470, [80, 290], 10)
tbl([['Pesaing', 'Tawaran', 'Celah untuk warung makan'],
     ['BukuWarung', 'Pembukuan, QRIS, produk digital; gratis', 'Catat manual; fokus luas'],
     ['BukuKas', 'Pembukuan UMKM, stok, laporan', 'Input manual'],
     ['Qasir', 'Kasir, fitur dasar gratis', 'Input per pesanan'],
     ['CatatKas', 'Buku kas; foto struk atau ketik', 'Mirip foto; stok menu dan pendampingan tidak disebut'],
     ['Dcatat Kasir', 'Kasir gratis, offline', 'Input per penjualan']], 450, 470, [80, 200, 190], 9.5)
card(40, 215, 880, 95, LORG)
para('<b>Jujur soal pembeda.</b> Foto nota sudah ada di pesaing seperti CatatKas. Pembeda yang dipertahankan: fokus warung makan, satu rekaman suara, penanda stok menu, pendampingan hari pertama. Belum diuji langsung. Harga paket berbayar pesaing belum diverifikasi.', 55, 205, 850, 12)
para('Sumber: Google Play (BukuWarung, Qasir, CatatKas, Dcatat Kasir, BukuKas), bukuwarung.com, Crunchbase.', 40, 105, 880, 9.5, GREYC)

# ===== 11 Kanal, konten, KPI
new('Kanal digital, kalender konten, dan KPI kampanye', '6. WhatsApp Business utama; Instagram/TikTok pendukung', 'PEMASARAN')
tbl([['Minggu', 'Konten (3 per minggu)'],
     ['1', 'Masalah "1 jam rekap"; Reels demo foto nota; undangan demo paguyuban'],
     ['2', 'Reels penanda stok; tutorial 1 suara; TikTok buku tulis vs Tumbuh.in'],
     ['3', 'Bukti (data uji nyata, kutipan izin); tips koreksi; TikTok rekap lengkap'],
     ['4', 'Penawaran uji + uang muka Rp10.000; cerita hari pertama; ajakan pilot']], 40, 470, [60, 400], 10.5)
tbl([['KPI (A)', 'Target'], ['Permintaan demo', '≥ 15 dari 25 dalam 14 hari (A3)'], ['Uang muka Rp10.000', '≥ 6 dari 10 (A1)'], ['Aktivasi rekap < 10 menit', '≥ 7 dari 10 (A2)'],
     ['Churn', '≤ 5% per bulan'], ['CAC', '≤ Rp30.000']], 530, 470, [150, 240], 10.5)
card(40, 230, 880, 75, SOFT)
para('<b>Mengapa WhatsApp:</b> segmen sudah memakainya, sebagian merasa gaptek (R-02), dan bantuan, demo, serta tagihan bisa lewat satu kanal. Video demo pendek menunjukkan foto nota menjadi rekap tanpa penjelasan panjang.', 55, 222, 850, 12)

# ===== 12 Keuangan 1
new(f'1 warung menyumbang {rp(CM)}/bln; impas di {BEP} warung', '7. Keuangan: harga pokok layanan, unit economics, titik impas', 'KEUANGAN')
tbl([['Indikator', 'Nilai'], ['Harga', 'Rp24.000/bulan (A)'], ['Biaya variabel', f'{rp(VAR)} (AI Rp6.900 + QRIS 0,7%)'], ['Margin kontribusi', rp(CM)], ['CAC', 'Rp30.000 (pendampingan)'],
     ['LTV', rp(LTV) + ' (churn 5%, A)'], ['LTV : CAC', f'{LTVCAC:.1f}'.replace('.', ',') + ' (bergantung asumsi)'], ['CAC payback', f'{PAYBACK:.1f} bulan'.replace('.', ',')],
     ['Biaya tetap hemat / penuh', f'{rp(FIX_H)} / {rp(FIX_P)}']], 40, 470, [140, 230], 10.5)
img(C['bep'], 440, 478, w=480)
card(40, 215, 880, 95, LORG)
para(f'<b>Titik impas.</b> Tahap hemat: {BEP} warung = {pct(BEP/25)} dari segmen awal (muat). Tahap penuh: {BEP_P} warung = {pct(BEP_P/25)} dari 25 dan {pct(BEP_P/58)} dari 58 (tidak muat). Tidak ada klaim layak komersial penuh sebelum harga dan pemakaian diuji. Alt 2 (Rp1.000/rekap): {A2_H} dan {A2_P} warung.', 55, 205, 850, 12)
para('Koreksi dari UTS: pendampingan Rp30.000 dipindah dari biaya variabel ke CAC (hindari hitung ganda). BEP UTS 12 dan 46 menjadi 11 dan 40. Sumber: file Excel Lampiran_Keuangan_Tumbuh-in.xlsx.', 40, 105, 880, 10, GREYC)

# ===== 13 Keuangan 2
new('Arus kas: modal Rp6 juta cukup; laba positif bulan ' + str(M_PROFIT), '7. Keuangan: arus kas, skenario, proyeksi 3 tahun', 'KEUANGAN')
img(C['cash'], 30, 490, w=430)
img(C['scen'], 480, 490, w=450)
rows = [['', 'Tahun 1', 'Tahun 2', 'Tahun 3'], ['Warung berbayar'] + [str(int(g('Ringkasan_3Thn', f'{c}4'))) for c in 'BCD']]
rows += [[lab] + [rp(g('Ringkasan_3Thn', f'{c}{r}')) for c in 'BCD'] for lab, r in (('Pendapatan', 5), ('Laba bersih', 8), ('Kas akhir', 10))]
tbl(rows, 40, 270, [150, 130, 130, 130], 10.5)
card(600, 270, 320, 150, SOFT)
para(f'<b>Skenario tahun 1</b><br/>Pesimis: laba {rp(g("Sensitivitas","F4"))}<br/>Moderat: {rp(g("Sensitivitas","F5"))}<br/>Optimis: {rp(g("Sensitivitas","F6"))}<br/>Kas terendah (moderat): {rp(g("Arus_Kas","B21"))}', 612, 258, 300, 11.5, lead=17)
para('Tahun 2-3 optimistis (butuh perluasan ke SWK lain; tahun 2 melebihi segmen awal 25). Semua angka = file Excel; semua pemeriksaan konsistensi OK.', 40, 105, 880, 10.5, GREYC)

# ===== 14 Tim, roadmap, ask
new('Tim, roadmap, dan kebutuhan', '8. Tim, roadmap, ask', 'TIM & ASK')
tbl([['Fase', 'Waktu', 'Kegiatan', 'Ukuran berhasil'], ['1 Validasi', 'Bln 1-2', 'Figma, uji pengguna, uang muka A1, paguyuban A3', 'A1 ≥ 6/10; A2 ≥ 7/10; SUS ≥ 68'],
     ['2 Pilot', 'Bln 3-6', 'Web sederhana; pendampingan 10 warung', f'{BEP} warung berbayar (bulan {M_BEP})'],
     ['3 Terbatas', 'Bln 7-12', 'Penanda stok; perkiraan belanja bila data cukup', f'{int(g("Ringkasan_3Thn","B4"))} warung; laba positif bulan {M_PROFIT}'],
     ['4 Perluasan', 'Thn 2-3', 'SWK lain di Surabaya (49 SWK); tahap penuh', f'Mendekati {BEP_P} warung']], 40, 470, [80, 60, 270, 200], 10.5)
card(40, 300, 430, 175, LGREEN)
para('<b>Ask</b>', 55, 288, 400, 15, GREEN_)
bullets(['Akses paguyuban SWK Srikana (lewat R-02)', '10 warung untuk uji uang muka dan pilot', 'Masukan mentor tentang harga'], 55, 262, 400, 12, 4)
card(490, 300, 430, 175, SOFT)
para('<b>Tim Kelompok 1 (6 mahasiswa D4 TI)</b>', 505, 288, 400, 13, NAVY_)
para('Pimpinan proyek, produk, teknologi, lapangan, pemasaran, keuangan. Setiap anggota berbicara dan siap tanya jawab lintas bagian.', 505, 262, 400, 12)
para(f'Pendanaan luar tidak dibutuhkan di tahap awal (kas terendah {rp(g("Arus_Kas","B21"))}). Dihitung ulang setelah hasil A1 dan A2.', 40, 105, 880, 11.5, GREYC)

# ===== 15 Referensi + AI
new('Referensi dan deklarasi penggunaan AI', '9. Referensi dan deklarasi AI (wajib, kriteria UAS butir 3)', 'REFERENSI')
bullets(['Kelompok 1 (2026). Laporan UTS Business Model Canvas Tumbuh.in. Univ. Airlangga.', 'Brooke (1996), SUS; Sauro (2011), A practical guide to SUS; Fitzpatrick (2013), The Mom Test.',
         'SIPUMKM Surabaya (data SWK); Midtrans (tarif QRIS); Harga Gemini API; Kurs JISDOR 6 Okt 2026 (via Laporan UTS).', 'PP 55/2022; UU 27/2022 (PDP).',
         'Google Play: BukuWarung, Qasir, CatatKas, Dcatat Kasir; Crunchbase: BukuKas; diakses 23 Nov 2026.'], 40, 470, 880, 12, 5)
card(40, 250, 880, 150, LORG)
para('<b>Deklarasi AI.</b> AI generatif dipakai sebagai alat bantu: menyusun draf business plan, laporan keuangan, dan deck dari Laporan UTS serta template mata kuliah; mengisi dan menghitung ulang model Excel; membuat grafik; mencari daftar pesaing awal. Substansi analisis, asumsi, dan angka menjadi tanggung jawab tim, yang memeriksa ulang terhadap file Excel dan sumber UTS.', 55, 238, 850, 12.5)
para('Setiap angka penting memiliki sumber atau tanda A (asumsi). Hasil uji pengguna dan A1 belum ada dan tidak diklaim.', 40, 80, 880, 11, GREYC)

# ===== Lampiran
state['n'] = 0; state['lamp'] = True
new('Lampiran 1. Biaya variabel dan biaya tetap', 'Dasar hitung (S = sumber, A = asumsi)', lamp=True)
tbl([['Komponen', 'Rp', 'Dasar'], ['Panggilan AI', '6.900', 'Gemini 3.5 Flash-Lite US$0,30/2,50 per juta token; kurs Rp17.917; 20 catatan x 26 hari + 4 ringkasan Batch (S/A)'],
     ['Penagihan QRIS', '168', '0,7% x Rp24.000 (S)'], ['WhatsApp', '0', 'WhatsApp Business biasa (A)'], ['Total variabel', num(VAR), ''],
     ['Biaya tetap hemat', num(FIX_H), 'Domain 5.000 + paket data dan transport 150.000 + cadangan 10% 16.000'],
     ['Biaya tetap penuh', num(FIX_P), '+ Supabase Pro Rp448.000 + cadangan 60.000'], ['CAC', '30.000', 'Transport pendampingan hari pertama (A)']], 40, 470, [140, 70, 650], 10.5)
new('Lampiran 2. Titik impas menurut harga', 'Warung untuk impas, Alt 1', lamp=True)
tbl([['Harga/bulan', 'Margin', 'BEP hemat (Rp171.000)', 'BEP penuh (Rp663.000)', 'BEP pesimis (Rp994.000)']] + [[rp(p), rp(v[0]), str(v[1]), str(v[2]), str(v[3])] for p, v in SENS.items()], 40, 470, [140, 140, 190, 190, 200], 11)
new('Lampiran 3. Asumsi kritis dan ambang keputusan', 'Ambang ditetapkan sebelum uji', lamp=True)
tbl([['ID', 'Rumusan', 'Hasil'], ['A1 Pendapatan', '≥ 6 dari 10 pemilik menyerahkan uang muka Rp10.000 untuk langganan ≥ Rp24.000/bulan setelah melihat simulasi layar', '[BELUM DIUJI]'],
     ['A2 Nilai', '≥ 7 dari 10 menyelesaikan rekap satu hari dari foto atau suara < 10 menit tanpa bantuan', '[BELUM DIUJI]'],
     ['A3 Kanal', '≥ 15 dari 25 pedagang SWK Srikana mendaftar uji coba dalam 14 hari lewat paguyuban', '[BELUM DIUJI]']], 40, 470, [110, 600, 150], 11)
new('Lampiran 4. Value Proposition Canvas', 'Sumber: Laporan UTS Kelompok 1', lamp=True)
img(IMG + r'\uts_image4.png', 140, 470, h=410)
cv.save()
print('pages', state['n'])

