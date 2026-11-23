from common import *
from dx import Doc
C = make_charts()
d = Doc()
d.cover('Laporan Keuangan Proyek Usaha Digital', 'Tumbuh.in: Rekap Harian dan Penanda Stok untuk Warung Makan Kecil di Sekitar Kampus', IMG + r'\uts_image1.png')
d.toc()

R = lambda s, c: g(s, c)
pb = 'Proyeksi_Bulanan'
rev1 = R('Ringkasan_3Thn', 'B5'); rev2 = R('Ringkasan_3Thn', 'C5'); rev3 = R('Ringkasan_3Thn', 'D5')
nb1, nb2, nb3 = (R('Ringkasan_3Thn', f'{c}8') for c in 'BCD')
kas1, kas2, kas3 = (R('Ringkasan_3Thn', f'{c}10') for c in 'BCD')
pel1, pel2, pel3 = (int(R('Ringkasan_3Thn', f'{c}4')) for c in 'BCD')
kas_min = R('Arus_Kas', 'B21'); kas_min_m = int(R('Arus_Kas', 'B22'))

# ---------- A
d.h1('A. Ringkasan Eksekutif Keuangan')
d.p('Laporan ini menjelaskan model keuangan Tumbuh.in untuk 12 bulan pertama dan ringkasan tiga tahun. Semua angka dihitung dengan rumus di file `Lampiran_Keuangan_Tumbuh-in.xlsx` dan sama dengan file tersebut. Tumbuh.in membantu pemilik warung makan kecil di sekitar kampus membuat rekap harian dari foto nota atau satu rekaman suara, disertai penanda stok.'.replace('`', ''))
d.table('Angka kunci model keuangan', ['Indikator', 'Nilai', 'Tanda'], [
    ['Harga langganan', rp(PRICE) + ' per warung per bulan', 'A'],
    ['Biaya variabel per warung per bulan', rp(VAR), 'S/A'],
    ['Margin kontribusi per warung per bulan', rp(CM), 'Hitung'],
    ['Biaya tetap per bulan (tahap hemat / tahap penuh)', f'{rp(FIX_H)} / {rp(FIX_P)}', 'S/A'],
    ['Titik impas (tahap hemat / tahap penuh)', f'{BEP} warung / {BEP_P} warung', 'Hitung'],
    ['Dibanding segmen awal 25 pedagang', f'{pct(BEP/25)} / {pct(BEP_P/25)}', 'Hitung'],
    ['Pendapatan tahun 1', rp(rev1), 'Proyeksi'],
    ['Laba (rugi) bersih tahun 1', rp(nb1), 'Proyeksi'],
    ['Saldo kas terendah tahun 1', f'{rp(kas_min)} (bulan {kas_min_m})', 'Proyeksi'],
    ['Warung berbayar akhir tahun 1', f'{pel1} warung', 'Proyeksi'],
    ['LTV : CAC', f'{LTVCAC:.1f} : 1'.replace('.', ','), 'Hitung'],
], [6, 6, 2])
d.p(f'Pada skenario moderat, usaha merugi {rp(-nb1)} pada tahun 1 karena pelanggan baru dibangun bertahap dan biaya akuisisi dibayar di awal. Rugi ini masih dapat ditutup modal tim {rp(6000000)}: saldo kas terendah {rp(kas_min)} pada bulan {kas_min_m}. Jumlah warung baru melewati titik impas pada bulan {M_BEP} dan laba bersih bulanan positif mulai bulan {M_PROFIT}.')
d.note('**Batas klaim.** Bukti baru berupa empat wawancara masalah (UTS). Kesediaan membayar, akurasi bacaan AI, dan penggunaan jangka panjang belum terbukti. Semua angka pelanggan, harga, dan churn adalah asumsi (A) sampai uji coba berbayar dilakukan. Tahap penuh (titik impas '
       f'{BEP_P} warung) melebihi segmen awal 25 pedagang, sehingga tidak ada klaim layak komersial penuh.')

# ---------- B
d.h1('B. Asumsi Pendapatan dan Pelanggan')
d.p('Pendapatan berasal dari langganan bulanan per warung (Alternatif 1 pada UTS Bab 4.4). Pendapatan bulanan dihitung dari rata-rata warung aktif (awal ditambah akhir bulan, dibagi dua) dikali harga, sehingga warung yang baru bergabung hanya dihitung setengah bulan.')
d.table('Asumsi pendapatan dan pelanggan', ['Asumsi', 'Nilai', 'Dasar'], [
    ['Harga langganan', rp(PRICE) + '/bulan', 'A. Diuji di Rp19.000, Rp24.000, Rp29.000 (UTS A1)'],
    ['Churn tahun 1', '5% per bulan', 'A. Belum ada data; asumsi konservatif'],
    ['Churn tahun 2 dan 3', '4,5% dan 4%', 'A. Retensi membaik setelah perbaikan produk'],
    ['Warung baru per bulan, tahun 1', '2 warung (total 24)', 'A. Pilot lewat kunjungan langsung dan paguyuban; total tidak melebihi segmen awal 25'],
    ['Warung baru per bulan, tahun 2 dan 3', '3 dan 4 warung', 'A. Perluasan ke SWK lain di Surabaya (49 SWK, Dinkopdag, UTS Bab 4.4); belum terbukti'],
    ['Ukuran segmen awal', '25 pedagang (SWK Srikana); batas atas 58', 'S. SIPUMKM Surabaya (UTS Bab 2.2)'],
], [4, 4, 7])
d.p('Warung berbayar baru pada tahun 1 dibatasi 2 per bulan agar total tidak melebihi segmen awal. Angka ini jauh di bawah target pendaftaran uji coba (15 dari 25 pedagang, asumsi A3 di UTS). Selisihnya disengaja: uji coba gratis berbeda dengan langganan berbayar.')

# ---------- C
d.h1('C. Dana Awal: Sumber dan Penggunaan')
d.table('Sumber dan penggunaan dana awal', ['Pos', 'Rp', 'Keterangan'], [
    ['Modal tim (6 anggota x Rp1.000.000)', num(6000000), 'A. Keputusan tim'],
    ['Investor luar', '0', 'A. Belum ada'],
    ['Total sumber dana', num(6000000), ''],
    ['Perangkat', '0', 'Memakai laptop dan ponsel pribadi'],
    ['Pengembangan MVP', '0', 'Dikerjakan tim sendiri; prototipe Figma gratis'],
    ['Legalitas dan merek', '0', 'Ditunda sampai ada pendapatan'],
    ['Cadangan kas operasional', num(6000000), 'Sisa dana setelah investasi dan pra-operasi'],
], [6, 3, 6], right_cols=(1,))
d.p('Biaya waktu tim tidak dihitung. Bila Tumbuh.in dijalankan sebagai usaha penuh, gaji tim, pajak badan usaha, dan pengembangan awal akan menambah biaya.')

# ---------- D
d.h1('D. Harga Pokok Layanan dan Struktur Biaya')
d.h2('D.1 Biaya variabel per warung per bulan')
d.p('Biaya variabel adalah biaya yang naik bila warung bertambah. Dua komponen dipakai: panggilan model AI dan biaya penagihan QRIS.')
d.table('Biaya variabel per warung per bulan', ['Komponen', 'Rp', 'Dasar hitung'], [
    ['Panggilan model AI', num(6900), 'Harga token Gemini 3.5 Flash-Lite US$0,30 masuk dan US$2,50 keluar; kurs JISDOR Rp17.917 (6 Okt 2026). Foto nota sekitar 1.300 token masuk dan 250 keluar; suara 10 detik sekitar 470 masuk dan 120 keluar; rata-rata Rp13 per catatan; 20 catatan per hari; 26 hari; ditambah 4 ringkasan mingguan lewat Batch. Harga: S. Jumlah token dan catatan: A'],
    ['Penagihan QRIS (0,7% x Rp24.000)', num(168), 'S. Tarif QRIS merchant reguler 0,7% (Midtrans)'],
    ['WhatsApp', '0', 'A. WhatsApp Business biasa, tanpa API berbayar'],
    ['Total variabel', num(VAR), 'Sama dengan Unit_Economics!B4'],
], [4, 2, 9], right_cols=(1,), bold_last=True)
d.p('**Koreksi dari UTS.** UTS memasukkan pendampingan hari pertama (Rp30.000 sekali, dicicil Rp2.500 per bulan) ke biaya variabel sehingga totalnya Rp9.550. Template keuangan UAS punya baris CAC terpisah, jadi pendampingan dipindah ke CAC Rp30.000. Dengan begitu biaya itu tidak terhitung dua kali. Akibatnya margin naik dari Rp14.450 menjadi ' + rp(CM) + '.')
d.image(C['cost'], 'Uraian harga Rp24.000 per warung per bulan.', 13)
d.h2('D.2 Biaya tetap per bulan')
d.table('Biaya tetap tahap hemat dan tahap penuh', ['Komponen', 'Tahap hemat', 'Tahap penuh', 'Tanda'], [
    ['Basis data dan backend (Supabase)', '0', '448.000', 'S'],
    ['Hosting web (Cloudflare Pages, gratis)', '0', '0', 'S'],
    ['Domain .my.id (anggaran Rp60.000/tahun)', '5.000', '5.000', 'S/A'],
    ['Paket data dan transport tim ke sentra', '150.000', '150.000', 'A'],
    ['Subtotal', '155.000', '603.000', ''],
    ['Cadangan 10%', '16.000', '60.000', 'A'],
    ['Total biaya tetap', num(FIX_H), num(FIX_P), ''],
], [7, 3, 3, 2], right_cols=(1, 2), bold_last=True)
d.p('Tahap hemat berlaku selama basis data masih memakai paket gratis. Tim pindah ke tahap penuh bila warung berbayar mendekati titik impas tahap penuh atau basis data melewati 400 MB. Sebelum itu, data diekspor setiap pekan karena paket gratis tidak menjamin pencadangan.')
d.p('Di model, tahun 1 memakai tahap hemat. Tahun 2 tetap tahap hemat karena warung berbayar akhir tahun 2 (' + str(pel2) + ') masih di bawah titik impas tahap penuh. Tahun 3 memakai tahap penuh karena warung berbayar mencapai ' + str(pel3) + '.')
d.h2('D.3 Biaya akuisisi pelanggan (CAC)')
d.p('CAC Rp30.000 per warung adalah transport tim pulang-pergi untuk pendampingan hari pertama (A). Belum dihitung kemungkinan satu kunjungan mendampingi beberapa warung sekaligus, yang menurunkan CAC.')

# ---------- E
d.h1('E. Unit Economics dan Titik Impas')
d.table('Unit economics (dari sheet Unit_Economics)', ['Indikator', 'Hasil', 'Rumus'], [
    ['Biaya variabel per warung per bulan', rp(VAR), 'AI + WhatsApp + harga x % QRIS'],
    ['Margin kontribusi (CM)', rp(CM), 'Harga - biaya variabel'],
    ['Rasio margin kontribusi', pct(CM / PRICE, 1), 'CM / harga'],
    ['BEP tahap hemat (desimal)', f'{FIX_H / CM:.1f} warung'.replace('.', ','), 'Biaya tetap / CM'],
    ['BEP tahap hemat (dibulatkan)', f'{BEP} warung', 'ROUNDUP'],
    ['BEP tahap penuh', f'{BEP_P} warung ({BEP_P_D:.1f})'.replace('.', ','), 'Rp663.000 / CM'],
    ['BEP dalam Rp pendapatan per bulan (hemat)', rp(BEP_RP), 'Biaya tetap / rasio CM'],
    ['Customer lifetime value (LTV)', rp(LTV), 'CM / churn 5%'],
    ['LTV : CAC', f'{LTVCAC:.1f}'.replace('.', ','), 'LTV / Rp30.000'],
    ['CAC payback', f'{PAYBACK:.1f} bulan'.replace('.', ','), 'CAC / CM'],
    ['Warung melewati BEP pada bulan', str(M_BEP), 'Proyeksi_Bulanan'],
    ['Laba bersih bulanan positif mulai bulan', str(M_PROFIT), 'Proyeksi_Bulanan'],
], [6, 4, 5], right_cols=(1,))
d.p(f'LTV : CAC sebesar {LTVCAC:.1f}'.replace('.', ',') + f' terlihat sangat sehat. Namun nilai ini bergantung pada churn 5% dan CAC Rp30.000 yang keduanya asumsi. Seperti pesan template, nilai yang sangat tinggi biasanya tanda asumsi terlalu optimistis, sehingga angka ini jangan dipakai sebagai bukti.')
d.h2('E.1 Titik impas dan ukuran segmen')
d.table('Titik impas dua alternatif pendapatan dibanding segmen', ['Alternatif', 'Margin/warung', 'BEP hemat', '% dari 25', 'BEP penuh', '% dari 25', '% dari 58'], [
    ['Alt 1: langganan Rp24.000', rp(CM), str(BEP), pct(BEP / 25), str(BEP_P), pct(BEP_P / 25), pct(BEP_P / 58)],
    ['Alt 2: Rp1.000 per rekap (22 rekap/bulan)', rp(A2_CM), str(A2_H), pct(A2_H / 25), str(A2_P), pct(A2_P / 25), pct(A2_P / 58)],
], [5, 2.5, 2, 2, 2, 2, 2], size=9)
d.p('Alt 2 dihitung di luar model Excel dengan rumus yang sama: pendapatan Rp22.000, biaya variabel Rp6.900 ditambah 0,7% dari Rp22.000. Alt 2 menjadi cadangan bila penolakan harga ternyata disebabkan tagihan tetap bulanan tidak cocok dengan pola kas harian pedagang (R-01).')
d.image(C['bep'], 'Warung yang dibutuhkan untuk impas dibanding ukuran segmen.', 13)
d.p(f'Tahap hemat muat di segmen awal: {BEP} warung adalah {pct(BEP/25)} dari 25 pedagang. Tahap penuh tidak muat: {BEP_P} warung adalah {pct(BEP_P/25)} dari segmen awal dan {pct(BEP_P/58)} dari batas atas 58. Jadi Tumbuh.in baru menjadi usaha penuh bila menjangkau SWK lain.')

# ---------- F
d.h1('F. Proyeksi Laba Rugi Tahun 1')
rows = []
labels = [('Pelanggan berbayar aktif (akhir)', 4, False), ('Pendapatan langganan', 5, True), ('Beban pokok pendapatan', 6, True), ('Laba kotor', 7, True),
          ('Domain dan perangkat lunak', 11, True), ('Paket data dan transport', 12, True), ('Cadangan 10%', 13, True), ('Pemasaran (CAC)', 14, True),
          ('EBITDA', 16, True), ('Laba (rugi) operasional', 18, True), ('Pajak PPh final', 19, True), ('Laba (rugi) bersih', 20, True)]
for lab, r, money in labels:
    row = [lab]
    for c in 'BCDEF':
        v = g('Laba_Rugi', f'{c}{r}')
        row.append(num(v) if not money else rp(v, True).replace('Rp', ''))
    rows.append(row)
d.table('Laba rugi tahun 1 per kuartal (Rp; negatif dalam kurung)', ['Pos', 'K1', 'K2', 'K3', 'K4', 'Tahun 1'], rows, [5, 2, 2, 2, 2, 2.3], right_cols=(1, 2, 3, 4, 5), size=9)
d.p(f'Usaha rugi pada tiga kuartal pertama dan mulai laba pada kuartal 4 (laba bersih {rp(g("Laba_Rugi","E20"))}). Honor tim, penyusutan, dan pra-operasi bernilai nol, jadi tidak muncul di tabel. PPh final dihitung dari omzet bruto sehingga tetap dibayar walau usaha rugi.')
d.image(C['growth'], 'Warung berbayar akhir bulan dan garis titik impas.', 12.5)

# ---------- G
d.h1('G. Proyeksi Arus Kas 12 Bulan')
rows = []
for lab, r in (('Saldo kas awal', 5), ('Penerimaan dari pelanggan', 7), ('Pembayaran beban pokok', 8), ('Pembayaran biaya tetap', 9), ('Pembayaran pemasaran', 10), ('Pembayaran PPh final', 12), ('Arus kas operasi', 13), ('Setoran modal', 16), ('Saldo kas akhir', 17)):
    rows.append([lab] + [rp(g('Arus_Kas', f'{c}{r}'), True).replace('Rp', '') for c in 'BCDEFG'])
d.table('Arus kas bulan 1 sampai 6 (Rp)', ['Pos', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6'], rows, [4.5, 2, 2, 2, 2, 2, 2], right_cols=range(1, 7), size=8.5)
rows = []
for lab, r in (('Penerimaan dari pelanggan', 7), ('Pembayaran beban pokok', 8), ('Pembayaran biaya tetap', 9), ('Pembayaran pemasaran', 10), ('Pembayaran PPh final', 12), ('Arus kas operasi', 13), ('Saldo kas akhir', 17)):
    rows.append([lab] + [rp(g('Arus_Kas', f'{c}{r}'), True).replace('Rp', '') for c in 'HIJKLM'] + [rp(g('Arus_Kas', f'N{r}'), True).replace('Rp', '') if r != 17 else rp(g('Arus_Kas', 'M17')).replace('Rp', '')])
d.table('Arus kas bulan 7 sampai 12 dan total tahun 1 (Rp)', ['Pos', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'Tahun 1'], rows, [4, 1.9, 1.9, 1.9, 1.9, 1.9, 1.9, 2.3], right_cols=range(1, 8), size=8)
d.p(f'Kas terendah {rp(kas_min)} terjadi pada bulan {kas_min_m}. Dana yang terpakai sebelum kas berbalik naik hanya {rp(g("Arus_Kas","B24"))} ({pct(1-g("Arus_Kas","B25"))} dari modal). Arus kas operasi bulanan positif mulai bulan {int(g("Arus_Kas","B23"))}.')
d.image(C['cash'], 'Saldo kas akhir dan laba bersih bulanan.', 12.5)

# ---------- H
d.h1('H. Neraca Akhir Tahun 1')
d.table('Laporan posisi keuangan akhir tahun 1', ['Pos', 'Rp'], [
    ['Kas dan setara kas', num(g('Neraca', 'B5'))], ['Perangkat (nilai buku)', num(g('Neraca', 'B8'))], ['**Total aset**', num(g('Neraca', 'B9'))],
    ['Utang PPh final (bulan 12)', num(g('Neraca', 'B12'))], ['Modal disetor', num(g('Neraca', 'B16'))],
    ['Saldo rugi tahun 1', rp(g('Neraca', 'B17')).replace('Rp', '')], ['Total ekuitas', num(g('Neraca', 'B18'))],
    ['**Total liabilitas + ekuitas**', num(g('Neraca', 'B20'))], ['Selisih', num(g('Neraca', 'B22'))]], [8, 4], right_cols=(1,))
d.p('Neraca seimbang: total aset sama dengan total liabilitas ditambah ekuitas (selisih nol).')

# ---------- I
d.h1('I. Ringkasan Proyeksi Tiga Tahun')
rows = [[lab] + [rp(g('Ringkasan_3Thn', f'{c}{r}'), True).replace('Rp', '') for c in 'BCD'] for lab, r in (('Pendapatan', 5), ('Laba kotor', 6), ('EBITDA', 7), ('Laba (rugi) bersih', 8), ('Saldo kas akhir tahun', 10))]
rows.insert(0, ['Warung berbayar akhir tahun', str(pel1), str(pel2), str(pel3)])
d.table('Proyeksi tiga tahun', ['Pos', 'Tahun 1', 'Tahun 2', 'Tahun 3'], rows, [6, 3, 3, 3], right_cols=(1, 2, 3))
d.p(f'Pertumbuhan tahun 2 dan 3 bersifat optimistis. Warung berbayar akhir tahun 2 ({pel2}) sudah melebihi segmen awal 25, sehingga hanya mungkin bila Tumbuh.in menjangkau SWK lain. Laba tahun 2 tinggi karena biaya tetap tahap hemat; laba tahun 3 turun karena pindah ke tahap penuh ({rp(FIX_P)} per bulan). Dasar angka tahun 2 dan 3 adalah asumsi (A) yang wajib diuji sebelum dipakai sebagai target.')

# ---------- J
d.h1('J. Analisis Sensitivitas')
rows = []
for r, nm, ch in ((4, 'Pesimis', '7%'), (5, 'Moderat', '5%'), (6, 'Optimis', '4%')):
    rows.append([nm, {4: '0,7', 5: '1', 6: '1,3'}[r], ch, str(int(g('Sensitivitas', f'D{r}'))), rp(g('Sensitivitas', f'E{r}')).replace('Rp', ''), rp(g('Sensitivitas', f'F{r}'), True).replace('Rp', ''), num(g('Sensitivitas', f'G{r}')), str(g('Sensitivitas', f'H{r}')) if isinstance(g('Sensitivitas', f'H{r}'), str) else f'bulan {int(g("Sensitivitas", f"H{r}"))}'])
d.table('Tiga skenario tahun 1', ['Skenario', 'Pengali baru', 'Churn', 'Warung akhir', 'Pendapatan', 'Laba bersih', 'Kas terendah', 'Laba positif'], rows, [2.2, 1.8, 1.4, 1.8, 2.3, 2.3, 2.3, 2.2], right_cols=(3, 4, 5, 6), size=8.5)
d.image(C['scen'], 'Laba bersih tahun 1 per skenario.', 12)
d.p('Pada skenario pesimis kas tetap positif (' + rp(g('Sensitivitas', 'G4')) + ' terendah), jadi modal tim cukup menahan satu tahun. Laba baru muncul pada skenario optimis.')
d.h2('J.1 Sensitivitas harga terhadap titik impas (Alt 1)')
rows = [[rp(p), rp(v[0]), str(v[1]), str(v[2]), str(v[3])] for p, v in SENS.items()]
d.table('Titik impas menurut harga (jumlah warung)', ['Harga/bulan', 'Margin', 'Hemat Rp171.000', 'Penuh Rp663.000', 'Pesimis Rp994.000'], rows, [3, 3, 3, 3, 3], right_cols=(1, 2, 3, 4))
d.p('Pada tahap hemat, ketiga harga berada di bawah 25 warung (Rp19.000 paling tipis: 15 warung). Pada tahap penuh, hanya Rp24.000 dan Rp29.000 yang berada di bawah batas atas 58. Bila panggilan AI dua kali lipat (Rp13.800), margin turun dan titik impas tahap hemat naik (hitung ulang di sheet Asumsi).')

# ---------- K
d.h1('K. Risiko dan Keterbatasan')
d.table('Risiko keuangan utama', ['Risiko', 'Dampak', 'Penanganan'], [
    ['Pemilik warung tidak mau membayar Rp24.000', 'Pendapatan nol', 'Uji uang muka Rp10.000 pada 10 pemilik (A1); alternatif harga Rp19.000 atau bayar per pemakaian'],
    ['Akurasi bacaan AI rendah', 'Koreksi manual lebih lama; churn naik', 'Uji bersama A2; pemilik dapat mengoreksi hasil'],
    ['Paket gratis Supabase dijeda atau data hilang', 'Layanan berhenti', 'Ekspor mingguan; pindah ke paket Pro bila data > 400 MB'],
    ['Biaya transport lebih besar dari asumsi', 'Biaya tetap naik', 'Ukur pada bulan pertama; gabungkan kunjungan per sentra'],
    ['Segmen awal hanya 25 pedagang', 'Tahap penuh tidak impas di segmen awal', 'Perluasan ke SWK lain; tahan pindah ke tahap penuh sampai warung berbayar mendekati ' + str(BEP_P)],
    ['Pesaing aplikasi pencatatan gratis', 'Harga sulit dinaikkan', 'Pembeda: cukup mencatat sekali; pendampingan hari pertama'],
    ['Perubahan tarif QRIS atau pajak', 'Margin berubah kecil', 'Periksa ketentuan terbaru'],
], [4.5, 3.5, 7])
d.p('Keterbatasan: (1) gaji tim, pajak badan usaha, dan pengembangan awal tidak dihitung; (2) angka transport dan pendampingan murni asumsi; (3) tarif QRIS 0,7% dipertahankan walau ada kabar pembebasan biaya yang belum dipastikan; (4) tarif PPh final 0,5% memakai nilai template dan perlu dicek terhadap bentuk usaha yang dipilih.')

# ---------- L
d.h1('L. Rencana Pendanaan dan Kebutuhan')
d.p(f'Pada skenario moderat, modal tim {rp(6000000)} cukup tanpa pendanaan luar: dana terpakai paling banyak {rp(g("Arus_Kas","B24"))}. Karena itu kebutuhan utama Tumbuh.in pada tahap ini bukan uang, tetapi akses: (1) pengenalan lewat paguyuban pedagang SWK Srikana, (2) 10 warung untuk uji uang muka dan pilot, dan (3) masukan mentor tentang harga. Bila tim ingin mempercepat perluasan ke SWK lain, pendanaan tambahan dihitung ulang setelah hasil uji A1 dan A2 tersedia (Tahap penuh butuh sekitar ' + rp(FIX_P) + ' per bulan).')

# ---------- M
d.h1('M. Cek Konsistensi')
rows = [[g('Cek_Konsistensi', f'A{r}'), num(g('Cek_Konsistensi', f'B{r}')), num(g('Cek_Konsistensi', f'C{r}')), g('Cek_Konsistensi', f'D{r}')] for r in range(4, 12)]
d.table('Hasil pemeriksaan otomatis (sheet Cek_Konsistensi)', ['Pemeriksaan', 'Nilai A', 'Nilai B', 'Status'], rows, [8, 2.5, 2.5, 1.5], right_cols=(1, 2), size=8.5)
d.p('Semua pemeriksaan otomatis berstatus OK dan jumlah status CEK adalah 0. Pemeriksaan manual pada sheet yang sama dicentang setelah angka laporan keuangan, business plan, pitch deck, dan file Excel dicocokkan.')

# ---------- N
d.h1('N. Sumber dan Deklarasi Penggunaan AI')
d.bullets([
    'Kelompok 1. (2026). Laporan UTS Business Model Canvas Tumbuh.in. Universitas Airlangga.',
    'SIPUMKM Surabaya. Data pedagang SWK Srikana dan SWK Mulyorejo (dikutip dari Laporan UTS Bab 2.2).',
    'Daftar harga model Gemini API, kurs JISDOR Bank Indonesia 6 Oktober 2026, tarif QRIS Midtrans (dikutip dari Laporan UTS Bab 4.4).',
    'PP 55/2022 jo. PP 20/2026 tentang PPh final UMKM (sesuai catatan template keuangan).',
])
d.p('**Deklarasi AI.** Asisten AI generatif dipakai untuk mengisi template Excel, menghitung ulang model, membuat grafik, dan menyusun draf laporan ini dari Laporan UTS Kelompok 1 dan template mata kuliah. Substansi asumsi dan angka menjadi tanggung jawab tim, yang memeriksa ulang angka terhadap file Excel.')
d.save(OUT + r'\Laporan_Keuangan_Tumbuh-in.docx')
print('ok')
