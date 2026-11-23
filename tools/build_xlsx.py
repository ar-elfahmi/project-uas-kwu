import openpyxl, sys, json
SRC = r'D:\08_CodeKuliah\project-uas-kwu\Salinan dari Format_Laporan_Keuangan_Proyek_Usaha_Digital.xlsx'
OUT = r'D:\08_CodeKuliah\project-uas-kwu\output\Lampiran_Keuangan_Tumbuh-in.xlsx'
P = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
wb = openpyxl.load_workbook(SRC)
a = wb['Asumsi']

def put(cell, val, src=None):
    a[cell] = val
    if src is not None:
        a['D' + cell[1:]] = src

a['A1'] = 'ASUMSI DASAR (input) - Tumbuh.in'
a['A2'] = ('Ubah hanya sel biru/kuning. Kolom D berisi dasar/sumber. F = fakta wawancara (R-01..R-04), '
           'S = sumber luar, A = asumsi tim. Semua angka mengikuti Laporan UTS Kelompok 1 kecuali yang ditandai koreksi UAS.')
a['A5'] = 'Harga langganan Tumbuh.in'
a['C5'] = 'Rp/warung/bln'
put('B5', 24000, 'A. Keputusan UTS Bab 4.4 (Alt 1). Akan diuji di Rp19.000, Rp24.000, Rp29.000; kesediaan membayar belum terbukti (asumsi kritis A1)')
put('B6', 0.05, 'A. Belum ada data; asumsi konservatif. Diperbarui setelah uji coba berbayar')
a['A7'] = 'Biaya akuisisi pelanggan (CAC) = pendampingan hari pertama'
put('B7', 30000, 'A. UTS Bab 4.4: transport pulang-pergi tim Rp30.000 per warung. Koreksi UAS: dipindah dari biaya variabel (dicicil Rp2.500) ke CAC agar tidak hitung ganda')
a['A9'] = 'Panggilan model AI (Gemini 3.5 Flash-Lite, foto/suara)'
put('B9', 6900, 'S/A. UTS Bab 4.4: harga token US$0,30 masuk/US$2,50 keluar, kurs JISDOR Rp17.917 (6 Okt 2026); 20 catatan/hari x 26 hari + 4 ringkasan Batch. Jumlah token dan catatan: A')
a['A10'] = 'Notifikasi WhatsApp (bantuan purna jual)'
put('B10', 0, 'A. Bantuan lewat WhatsApp Business biasa, tanpa API berbayar pada tahap awal (UTS blok Hubungan Pelanggan)')
a['A11'] = 'Biaya penagihan QRIS'
put('B11', 0.007, 'S. Tarif QRIS merchant reguler 0,7% (Midtrans), UTS Bab 4.4')
put('B13', 0.005, 'S. PP 55/2022 jo. PP 20/2026 (template). Dipakai konservatif; periksa ketentuan terbaru dan status badan usaha sebelum dipakai')
put('B14', 48, 'Kebijakan template: garis lurus 4 tahun. Tidak berpengaruh karena perangkat Rp0')
a['A16'] = 'Modal tim (6 anggota x Rp1.000.000)'
put('B16', 6000000, 'A. Keputusan tim UAS: modal sendiri, tanpa investor')
a['A17'] = 'Investasi pihak luar (ekuitas)'
put('B17', 0, 'A. Belum ada investor')
a['A19'] = 'Perangkat - memakai laptop dan ponsel pribadi anggota'
put('B19', 0, 'A. Tidak ada pembelian perangkat')
a['A20'] = 'Pengembangan MVP (dibuat sendiri oleh tim; Figma gratis)'
put('B20', 0, 'A. Tidak ada pembayaran freelancer; waktu tim tidak dihitung')
a['A21'] = 'Legalitas dan merek (ditunda sampai ada pendapatan)'
put('B21', 0, 'A. Ditunda; PT Perorangan dipertimbangkan setelah pilot berbayar')
a['A25'] = 'Honor tim inti (tidak ada; tim mahasiswa)'
put('B25', 0, 'A. UTS Bab 4.4: tim tidak menggaji diri sendiri. Bila dijalankan sebagai usaha penuh, komponen ini menambah biaya (lihat Sensitivitas)')
a['A26'] = 'Domain .my.id (Rp60.000/tahun); Supabase dan Cloudflare Pages paket gratis'
put('B26', 5000, 'S/A. UTS Bab 4.4: domain .my.id mulai Rp16.900/tahun, dianggarkan Rp60.000; hosting dan basis data paket gratis tahap hemat')
a['A27'] = 'Langganan perangkat lunak berbayar'
put('B27', 0, 'A. Memakai paket gratis (Figma, repo, email)')
a['A28'] = 'Paket data dan transport tim ke sentra'
put('B28', 150000, 'A. UTS Bab 4.4: kunjungan digabung per sentra. Angka paling rawan, diukur pada bulan pertama')
a['A29'] = 'Cadangan 10% biaya tetap'
put('B29', 16000, 'A. UTS Bab 4.4: 10% dari Rp155.000, dibulatkan. Total biaya tetap = Rp171.000 (tahap hemat)')
new = P.get('new', [2] * 12)
for i, v in enumerate(new):
    a.cell(row=33, column=2 + i, value=v)
a['D2'] = None
a['A33'] = 'Warung berbayar baru (orang/warung)'
a['B36'] = P.get('y2new', 3)
a['C36'] = P.get('y3new', 4)
a['D36'] = ('A. Perluasan ke SWK lain di Surabaya (49 SWK menurut Dinkopdag, UTS Bab 4.4) setelah segmen awal 25 pedagang; '
            'kanal: rekomendasi warung pilot dan paguyuban. Belum terbukti')
a['B37'] = 0.045
a['C37'] = 0.04
a['D37'] = 'A. Retensi membaik setelah perbaikan produk (nilai template dipertahankan)'
a['B38'] = P.get('y2fix', 663000)
a['C38'] = P.get('y3fix', 663000)
a['D38'] = 'A. UTS Bab 4.4: tahap penuh (Supabase Pro US$25) Rp663.000/bln, dipicu pelanggan mendekati 40-46 warung atau basis data > 400 MB'
a['B41'] = 0.7
a['D41'] = 1.3
a['B42'] = 0.07
a['D42'] = 0.04

# Label sheet lain
pet = wb['Petunjuk']
pet['A4'] = 'Usaha'
pet['B4'] = ('Tumbuh.in - rekap harian dan penanda stok untuk warung makan kecil di sekitar kampus (Kelompok 1, UAS Kewirausahaan Bidang TI). '
             'Angka berasal dari Laporan UTS dan asumsi tim; tanda F/S/A ada di kolom D sheet Asumsi. Belum ada data uji berbayar.')
pet['B37'] = 'Biaya pengembangan MVP (Rp0, dikerjakan tim sendiri) dibebankan di bulan 1; perangkat (Rp0) disusutkan garis lurus.'
pet['B38'] = 'Tarif PPh final 0,5% mengacu pada PP 55/2022 jo. PP 20/2026; dipakai konservatif, periksa ketentuan terbaru dan bentuk usaha sebelum dipakai.'
pb = wb['Proyeksi_Bulanan']
pb['A13'] = 'Beban pokok = rata-rata x (panggilan AI + WA) + pendapatan x % penagihan QRIS'
pb['A15'] = 'Honor tim inti'
pb['A16'] = 'Domain dan langganan perangkat lunak'
pb['A17'] = 'Paket data dan transport tim'
pb['A18'] = 'Cadangan 10%'
wb['Unit_Economics']['C4'] = 'panggilan AI + WhatsApp + harga x % penagihan QRIS'
lr = wb['Laba_Rugi']
lr['A6'] = 'Beban pokok pendapatan (panggilan AI, WhatsApp, penagihan QRIS)'
lr['A10'] = '  Honor tim inti'
lr['A11'] = '  Domain dan langganan perangkat lunak'
lr['A12'] = '  Paket data dan transport tim'
lr['A13'] = '  Cadangan 10%'
lr['A15'] = 'Beban pra-operasi (pengembangan MVP, legalitas)'
wb['Cek_Konsistensi']['A16'] = 'Harga, biaya AI, dan tech stack konsisten dengan Laporan UTS Bab 4.4 dan dokumen prototipe.'
for r in P.get('tick', []):
    wb['Cek_Konsistensi']['D%d' % r] = '☑'
wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print('saved')
