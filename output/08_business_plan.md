# Business Plan Tumbuh.in (versi teks)

Versi markdown dari `Business_Plan_Tumbuh-in.docx` (sumber utama untuk pengumpulan). Angka sama dengan `Lampiran_Keuangan_Tumbuh-in.xlsx`.

BUSINESS PLAN FINAL

KEWIRAUSAHAAN BIDANG TI (FVK25612002)

Tumbuh.in: Rekap Harian dan Penanda Stok untuk Warung Makan Kecil di Sekitar Kampus

Dosen Pengampu:

Nambi Sembilu, S.Kom., M.Kom.

Disusun oleh Kelompok 1:

Alung Destantio Cahya Utama Putra (434241001)

Daffa Eka Sujianto (434241004)

Nabil Hakim Alfikri (434241055)

Muhammad Javier Rakha Abhista (434241021)

Muhammad Reyhan Ammar (434241061)

Alfiyan Rasyid El-Fahmi (434241047)

PROGRAM STUDI D4 TEKNIK INFORMATIKA

FAKULTAS VOKASI

UNIVERSITAS AIRLANGGA

SURABAYA

GASAL 2026/2027

DAFTAR ISI

(Daftar isi terisi saat file dibuka di Word: pilih Yes pada pertanyaan pembaruan, atau klik kanan lalu Update Field.)


## Bab 1. Ringkasan Eksekutif
Pemilik warung makan dan kedai kecil di sekitar kampus tiap malam menghitung uang dari buku atau perkiraan. Dua dari empat pemilik yang kami wawancarai menghabiskan 60 sampai 90 menit per hari untuk rekap. Dua lainnya tidak mencatat, sehingga laba harian hanya ditebak. Tiga dari empat pernah kehabisan menu atau bahan sebelum tutup karena stok sisa tidak terlihat.

Tumbuh.in adalah aplikasi web ringan. Pemilik memotret nota atau merekam satu pesan suara saat senggang. Aplikasi menyusun rekap harian (tunai dan QRIS) dan penanda stok yang hampir habis. Pemilik bisa mengoreksi hasilnya. Berbeda dari aplikasi kasir, pemilik tidak perlu mengetuk layar untuk setiap pesanan saat ramai. Target waktu rekap di bawah 10 menit adalah asumsi yang belum diuji.


*Tabel 1. Ringkasan bisnis*

| Aspek | Isi |
|---|---|
| Segmen awal | 25 pedagang SWK Srikana, Surabaya (SIPUMKM); batas atas 58 bila SWK Mulyorejo ikut |
| Harga | Langganan Rp24.000 per warung per bulan (A); cadangan Rp1.000 per rekap |
| Biaya tetap | Rp171.000 per bulan (tahap hemat); Rp663.000 (tahap penuh) |
| Titik impas | 11 warung (tahap hemat, 44% dari segmen awal); 40 warung (tahap penuh) |
| Proyeksi tahun 1 | 17 warung berbayar, pendapatan Rp2.868.000, rugi bersih Rp762.966; kas terendah Rp5.149.896 |
| Modal | Rp6.000.000 dari tim; tidak butuh investor pada tahap awal |
| Kebutuhan (ask) | Akses paguyuban pedagang, 10 warung pilot, masukan mentor tentang harga |

> Batas klaim. Bukti yang ada: empat wawancara masalah (tiga di satu sentra). Itu mendukung kecocokan pelanggan dan masalah pada tahap awal. Kecocokan solusi, kesediaan membayar, akurasi AI, dan kelayakan komersial penuh belum terbukti. Setiap angka ditandai F (fakta wawancara), S (sumber luar), atau A (asumsi tim).


## Bab 2. Masalah dan Bukti Validasi

### 2.1 Cara mengumpulkan bukti
Tim mewawancarai empat pemilik usaha makanan dan minuman pada 13 Oktober 2026 dengan delapan pertanyaan berpola Mom Test. Pertanyaan menanyakan kejadian nyata terakhir, bukan pendapat tentang ide. Semua responden setuju direkam dan bersedia dihubungi kembali. Responden dirujuk dengan kode R-01 sampai R-04; nama dan usaha tidak ditulis.


*Tabel 2. Responden wawancara*

| Kode | Jenis usaha | Lokasi | Cara mencatat sekarang |
|---|---|---|---|
| R-01 | Warung makan dan minuman | SWK Srikana | Tidak dicatat; laba ditebak dari saldo QRIS |
| R-02 | Kedai makan, pengurus paguyuban | SWK Srikana | Buku tunai, mutasi bank untuk QRIS; rekap tiap malam sekitar 1 jam |
| R-03 | Stand makanan | SWK Srikana | Tidak dicatat; hitung global saat tutup |
| R-04 | Warung kopi malam | Dekat kos | Buku tulis, 1 sampai 1,5 jam; pernah mencoba POS lalu berhenti |


### 2.2 Temuan
- Rekap dan laba (4 dari 4): R-02 sekitar 60 menit per malam, R-04 sekitar 90 menit; R-01 dan R-03 tidak mencatat.
- Kehabisan (3 dari 4): R-01, R-02, R-04 pernah. R-02: "Pernah, sering."
- Alat lama gagal: R-04 pernah memakai POS, tetapi penjualan jadi lebih lama sehingga kembali ke buku.
- Pola ramai-sepi berbeda per warung: perkiraan harus per warung, bukan satu aturan umum.

*Gambar 1. Matriks temuan wawancara R-01 sampai R-04 (n = 4). Sumber: Laporan UTS Kelompok 1.*


*Tabel 3. Kutipan verbatim responden*

| Kode | Menit | Kutipan | Arti |
|---|---|---|---|
| R-01 | 00:54 | "Gak ate dicatet wes. Gak ate dicatet, apa dicatet." | Tidak akan dicatat; apanya yang dicatat |
| R-02 | 14:15 | "Wis... satu jam lah." | Menotal catatan tunai setelah tutup sekitar satu jam |
| R-04 | 02:44 | "Soalnya kita tidak bisa melihat barang menu yang stoknya tinggal berapa dan untuk betulnya berapa." | Sisa stok menu tidak terlihat |
| R-04 | 07:00 | "Dulu pernah nyoba Mas, pakai aplikasi yaitu POS... jadinya lebih lama penjualannya. Jadinya saya tidak memakai lagi." | POS ditinggalkan karena memperlambat |


### 2.3 Pernyataan masalah
> Pemilik warung makan dan kedai kecil di sekitar kampus, setiap hari sesudah tutup, harus menghitung uang dari buku atau perkiraan tanpa catatan penjualan yang tersusun, dan saat jualan tidak tahu menu atau bahan mana yang hampir habis. Akibatnya dua dari empat responden menghabiskan 60 sampai 90 menit per hari untuk rekap (R-02, R-04), dua lainnya tidak tahu laba harian (R-01, R-03), dan tiga dari empat pernah kehabisan menu atau bahan sebelum tutup (R-01, R-02, R-04).


### 2.4 Yang belum terbukti
Bukti baru berasal dari empat wawancara. Kesediaan membayar belum ditanyakan. Karena itu tim menetapkan tiga asumsi kritis yang diuji sebelum klaim apa pun dibuat (Bab 9).


## Bab 3. Solusi dan Value Proposition

### 3.1 Pernyataan nilai
> Untuk pemilik warung makan dan kedai kecil di sekitar kampus yang tiap malam menghabiskan 60 sampai 90 menit merekap uang atau tidak tahu laba harian dan menu apa yang hampir habis, Tumbuh.in memberikan rekap harian tunai dan QRIS dari foto nota atau satu rekaman suara, disertai penanda stok, dengan target waktu rekap di bawah 10 menit. Berbeda dari buku tulis dan aplikasi kasir yang menuntut input tiap pesanan, pemilik cukup mencatat sekali saat senggang dan dapat mengoreksi hasilnya.


### 3.2 Fitur dan sasaran

*Tabel 4. Sasaran pelanggan yang dilayani*

| Kode | Hambatan | Fitur Tumbuh.in | Bukti |
|---|---|---|---|
| H1 | Rekap 60-90 menit atau laba tidak diketahui | Rekap harian dari foto nota atau suara; pemilik mengoreksi | R-01 sampai R-04 (4 dari 4) |
| H2 | Menu atau bahan habis tanpa diketahui | Penanda stok menipis | R-01, R-02, R-04 |
| H3 | Alat lama lambat atau rumit | Satu layar; tanpa input per pesanan | R-04 |
| H4 | Makanan terbuang | Tidak dilayani sekarang (cadangan) | Nilai kecil |
| H5 | QRIS masuk bertahap, rekonsiliasi sulit | Tidak dilayani sekarang (cadangan) | 1 dari 4 |

Perkiraan belanja besok adalah fitur lanjutan yang baru dibuat setelah ada data catatan. Alasannya: dua dari empat responden tidak mencatat, jadi tidak ada data untuk memprediksi (Refleksi UTS).


*Gambar 2. Value Proposition Canvas. Sumber: Laporan UTS Kelompok 1.*


*Gambar 3. Alur kerja malam hari: sekarang dan dengan Tumbuh.in (rancangan; target belum diuji).*


### 3.3 Prototipe
Prototipe berupa Figma klik-tembus dengan data contoh (bukan data pelanggan nyata dan tanpa AI sungguhan). Prototipe memiliki empat layar:

- Layar 1, Ambil nota: tombol foto nota dan tombol rekam suara.
- Layar 2, Periksa hasil: daftar catatan yang terbaca; pemilik dapat memperbaiki angka dan nama menu.
- Layar 3, Rekap harian: uang tunai, QRIS, pengeluaran, laba hari itu, dan lama proses.
- Layar 4, Stok menipis: daftar menu atau bahan yang hampir habis.
Tautan prototipe: [ISI: tautan Figma yang dibuat tim]. Tautan wajib diisi sebelum pengumpulan.


## Bab 4. Model Bisnis

*Tabel 5. Business Model Canvas Tumbuh.in (sesuai UTS dengan koreksi UAS)*

| Blok | Isi | Tanda |
|---|---|---|
| Segmen pelanggan | Pemilik warung makan dan kedai kecil di sekitar kampus (SWK Srikana dulu). Subsegmen A sudah mencatat manual (R-02, R-04); B belum mencatat (R-01, R-03). Pembayar dan pengambil keputusan: pemilik | F/S/A |
| Value proposition | Rekap malam tanpa menulis ulang; penanda stok; cepat dan mudah tidak seperti POS lama; target rekap < 10 menit | F/A |
| Kanal | Kunjungan langsung ke sentra; rekomendasi paguyuban; demo dengan nota milik sendiri; web tanpa instal; WhatsApp purna jual | A |
| Hubungan pelanggan | Pendampingan hari pertama, lalu swalayan satu layar; bantuan WhatsApp; pemilik mengoreksi hasil AI | A |
| Arus pendapatan | Alt 1 langganan Rp24.000/bulan (diuji di Rp19.000, 24.000, 29.000). Alt 2 Rp1.000 per rekap (cadangan). Freemium gugur: tiap catatan memanggil AI | A |
| Sumber daya kunci | Model AI baca foto dan suara (API pihak ketiga); aplikasi web dan basis data; tim; akses ke 4 responden | S/A/F |
| Aktivitas kunci | Mengembangkan dan menguji akurasi baca foto dan suara; pendampingan hari pertama; kunjungan lapangan dan pengumpulan data pola harian | A |
| Kemitraan kunci | Penyedia AI dan hosting; paguyuban pedagang; warung pilot (R-02, R-04 kandidat); penyedia QRIS | S/A |
| Struktur biaya | Tetap Rp171.000/bulan (hemat), Rp663.000 (penuh); variabel Rp7.068 per warung; CAC Rp30.000 | S/A |

Dari 33 isian kanvas pada UTS, 7 bertanda F, 4 bertanda S, dan 22 bertanda A. Kanvas penuh asumsi pada tahap ini wajar. Masalah muncul bila asumsi ditandai fakta tanpa dasar, dan tim tidak melakukannya.


### 4.1 Perbandingan dua alternatif pendapatan

*Tabel 6. Alt 1 dan Alt 2*

| Pertimbangan | Alt 1: langganan | Alt 2: per pemakaian |
|---|---|---|
| Titik impas | 11 warung (hemat), 40 (penuh) | 12 (hemat), 45 (penuh) |
| Pola kas segmen | Tagihan tetap kurang cocok dengan uang harian (R-01) | Mengikuti pemakaian harian |
| Penagihan | Satu tagihan per bulan | Perlu hitung hari aktif |
| Kemudahan uji | Cukup 10 pemilik, satu kunjungan | Butuh beberapa pekan |

Keputusan sementara: uji Alt 1 lebih dulu. Alt 2 menjadi cadangan bila penolakan disebabkan tagihan tetap tidak cocok dengan pola kas harian.


## Bab 5. Rencana Operasional

### 5.1 Alur kerja layanan

*Tabel 7. Alur layanan Tumbuh.in*

| Tahap | Kegiatan | Penanggung jawab |
|---|---|---|
| 1. Kenalan | Tim memperkenalkan lewat paguyuban atau kunjungan; demo dengan satu foto nota milik pemilik | Tim lapangan |
| 2. Pendampingan hari pertama | Tim menemani pemilik memotret nota dan membaca rekap; biaya Rp30.000 transport | Tim lapangan |
| 3. Pemakaian harian | Pemilik memotret nota atau merekam suara saat senggang; AI menyusun rekap; pemilik mengoreksi | Pemilik |
| 4. Bantuan | Pertanyaan lewat WhatsApp | Tim dukungan |
| 5. Penagihan | Tagihan bulanan lewat QRIS | Tim keuangan |
| 6. Evaluasi mingguan | Cek akurasi baca, churn, dan keluhan; ekspor data mingguan | Tim produk |


### 5.2 Teknologi
- Aplikasi web responsif, tanpa instal (Cloudflare Pages, paket gratis).
- Basis data Supabase (paket gratis; Pro US$25 bila data > 400 MB atau warung berbayar mendekati 40).
- Model AI Gemini 3.5 Flash-Lite lewat API. Foto dan suara tidak disimpan, hanya teks hasil bacaan (sekitar 0,5 KB per catatan).
- Data usaha pelanggan tidak dikirim lewat paket gratis Gemini karena konten paket gratis dipakai penyedia untuk perbaikan produk.

### 5.3 Tim dan peran
Tim terdiri atas enam mahasiswa D4 Teknik Informatika. Pembagian peran di bawah menjadi usulan; tim mengisi nama penanggung jawab.


*Tabel 8. Peran tim*

| Peran | Tugas | Penanggung jawab |
|---|---|---|
| Pemimpin proyek | Koordinasi, jadwal, hubungan dengan paguyuban | [ISI: nama] |
| Produk dan prototipe | Figma, uji pengguna, perbaikan | [ISI: nama] |
| Teknologi | Aplikasi web, integrasi AI, ekspor data | [ISI: nama] |
| Lapangan | Kunjungan, pendampingan hari pertama | [ISI: nama] |
| Pemasaran | Konten, WhatsApp Business, KPI kampanye | [ISI: nama] |
| Keuangan | Model keuangan, penagihan, laporan | [ISI: nama] |


### 5.4 Pemicu pindah dari tahap hemat ke tahap penuh
Tahap hemat memakai paket gratis dan biaya tetap Rp171.000 per bulan. Tim pindah ke tahap penuh (Rp663.000 per bulan) bila warung berbayar mendekati 40 atau basis data melewati 400 MB. Sampai saat itu, risiko hilangnya data ditutup dengan ekspor mingguan.


## Bab 6. Strategi Pemasaran

### 6.1 Segmentasi, target, dan positioning (STP)

*Tabel 9. STP Tumbuh.in*

| Unsur | Isi |
|---|---|
| Segmentasi | Berdasarkan perilaku mencatat: (A) sudah mencatat manual 60-90 menit per hari; (B) belum mencatat, laba ditebak. Kedua subsegmen sama-sama pemilik warung makan di sekitar kampus |
| Target | Subsegmen A dulu (pengguna awal dengan workaround kuat: R-04, R-02), lalu B. Wilayah: SWK Srikana (25 pedagang) |
| Positioning | Satu-satunya pencatat untuk warung makan yang cukup dipakai sekali saat senggang lewat foto nota atau suara, dengan pendampingan hari pertama (klaim pembeda; belum terbukti terhadap semua pesaing, lihat 6.4) |

> Positioning statement. Bagi pemilik warung makan kecil yang lelah merekap tiap malam, Tumbuh.in adalah pencatat harian yang cukup dipakai sekali dari foto nota atau suara. Tidak seperti aplikasi kasir yang menuntut input tiap pesanan, Tumbuh.in tidak memperlambat penjualan saat ramai.


### 6.2 Bauran pemasaran 7P

*Tabel 10. 7P Tumbuh.in*

| P | Penerapan |
|---|---|
| Product | Rekap harian dari foto nota atau suara; penanda stok; koreksi oleh pemilik. Perkiraan belanja menyusul |
| Price | Rp24.000 per warung per bulan; uji di Rp19.000 dan Rp29.000; uang muka uji Rp10.000. Rp1.000 per rekap sebagai cadangan |
| Place | Web tanpa instal; distribusi lewat kunjungan langsung ke sentra dan paguyuban |
| Promotion | Demo dengan nota milik sendiri; WhatsApp Business; video demo pendek di Instagram dan TikTok; rekomendasi paguyuban |
| People | Tim lapangan yang mendampingi hari pertama; bantuan WhatsApp; pengguna awal sebagai referensi |
| Process | Alur lima langkah: kenalan, pendampingan, pemakaian harian, bantuan, penagihan (Bab 5) |
| Physical evidence | Prototipe Figma, tangkapan layar rekap, kutipan pengguna (dengan izin, tetap memakai kode), contoh nota dan hasil rekap |


### 6.3 Harga
Harga Rp24.000 dipilih dari titik impas tahap hemat (11 warung, 44% dari segmen awal). Pada Rp19.000, tahap hemat butuh 15 warung dan masih muat di segmen awal. Tidak ada data kesediaan membayar. Karena itu harga diuji dengan uang muka Rp10.000.


*Tabel 11. Titik impas menurut harga (Alt 1)*

| Harga/bulan | Margin | BEP hemat | BEP penuh |
|---|---|---|---|
| Rp19.000 | Rp11.967 | 15 | 56 |
| Rp24.000 | Rp16.932 | 11 | 40 |
| Rp29.000 | Rp21.897 | 8 | 31 |


### 6.4 Pesaing
Tim mencari pesaing nyata di Google Play dan situs resmi pada 23 November 2026. Harga paket berbayar tiap pesaing belum diverifikasi tim, sehingga tidak ditulis.


*Tabel 12. Peta pesaing*

| Pesaing | Yang ditawarkan | Kelemahan terhadap segmen warung makan | Sumber |
|---|---|---|---|
| BukuWarung | Pembukuan digital, QRIS, produk digital, pembiayaan; platform gratis untuk UMKM | Catat transaksi manual; fokus luas (agen pembayaran, penjualan pulsa); belum terlihat input dari foto nota atau suara di deskripsi toko | Google Play; bukuwarung.com |
| BukuKas | Pembukuan UMKM: catat transaksi, laporan otomatis, kelola stok barang | Input manual per transaksi | Google Play; Crunchbase |
| Qasir | Aplikasi kasir (POS) dengan fitur dasar gratis dan laporan penjualan | Input per pesanan, jenis alat yang ditinggalkan R-04 | Google Play |
| CatatKas | Buku kas; catat dari foto struk atau ketik seperti chat | Mirip dalam input foto. Deskripsi toko menyebut pribadi, keluarga, RT, dan komunitas; stok menu warung dan pendampingan tidak disebut | Google Play |
| Dcatat Kasir | Kasir gratis, stok, offline | Input per penjualan | Google Play |

Kesimpulan jujur. Fitur foto nota sudah ada di pesaing seperti CatatKas. Pembeda Tumbuh.in yang masih bisa dipertahankan adalah fokus warung makan, satu rekaman suara, penanda stok menu, dan pendampingan hari pertama. Tim belum menguji pesaing langsung, sehingga klaim pembeda diuji lewat uji pengguna (Bab 9). Pesaing gratis juga menekan harga, jadi harga Rp24.000 harus dibenarkan oleh waktu rekap yang lebih singkat.

Sumber pesaing: Google Play (BukuWarung, Qasir, CatatKas, Dcatat Kasir, BukuKas), bukuwarung.com, Crunchbase. Diakses 23 November 2026.


## Bab 7. Kanal Digital, Kalender Konten, dan Kpi

### 7.1 Kanal

*Tabel 13. Kanal digital*

| Kanal | Peran | Alasan |
|---|---|---|
| WhatsApp Business | Utama: demo, bantuan, penagihan, grup paguyuban | Segmen sudah memakai WhatsApp; sebagian merasa gaptek (R-02) |
| Instagram Reels dan TikTok | Pendukung: video demo 30 detik | Menunjukkan foto nota menjadi rekap; murah |
| Google Maps / profil usaha | Opsional setelah pilot | Belum diuji |


### 7.2 Kalender konten 4 minggu

*Tabel 14. Kalender konten (tiga unggahan per minggu)*

| Minggu | Kanal | Tema | Isi |
|---|---|---|---|
| 1 | WhatsApp / IG | Masalah | Cerita "satu jam rekap tiap malam" (tanpa nama); ajakan demo |
| 1 | IG Reels | Demo | Foto nota menjadi rekap dalam 30 detik |
| 1 | WhatsApp paguyuban | Ajakan | Undangan demo di pertemuan pedagang |
| 2 | IG Reels | Stok | Penanda menu hampir habis |
| 2 | WhatsApp | Tutorial | Cara merekam satu suara |
| 2 | TikTok | Perbandingan | Buku tulis vs Tumbuh.in |
| 3 | WhatsApp | Bukti | Hasil uji (hanya data nyata) dan kutipan pengguna dengan izin |
| 3 | IG | Tips | Cara mengoreksi hasil bacaan |
| 3 | TikTok | Demo | Rekap harian lengkap |
| 4 | WhatsApp | Penawaran | Uji coba dan uang muka Rp10.000 |
| 4 | IG | Cerita | Hari pertama pendampingan |
| 4 | WhatsApp | Penutup | Ajakan daftar pilot |


### 7.3 KPI kampanye

*Tabel 15. KPI (semua target adalah asumsi A)*

| KPI | Target | Cara ukur |
|---|---|---|
| Permintaan demo | ≥ 15 dari 25 pedagang dalam 14 hari lewat paguyuban (asumsi A3) | Catatan pendaftaran |
| Uang muka Rp10.000 | ≥ 6 dari 10 pemilik (asumsi A1) | Pembayaran QRIS |
| Aktivasi | ≥ 7 dari 10 menyelesaikan rekap < 10 menit tanpa bantuan (asumsi A2) | Uji pengguna |
| Retensi mingguan | Churn ≤ 5% per bulan (asumsi model) | Warung yang berhenti |
| Biaya per warung baru | ≤ Rp30.000 (CAC model) | Transport per pendampingan |


## Bab 8. Rencana Keuangan
Rincian lengkap ada di Laporan Keuangan dan file Excel Lampiran_Keuangan_Tumbuh-in.xlsx. Bab ini merangkum angka utama.


*Tabel 16. Ringkasan keuangan*

| Indikator | Nilai |
|---|---|
| Biaya variabel per warung | Rp7.068 (AI Rp6.900 + QRIS Rp168) |
| Margin kontribusi | Rp16.932 |
| CAC | Rp30.000 (pendampingan hari pertama) |
| LTV : CAC | 11,3 : 1 (bergantung asumsi churn 5%) |
| BEP tahap hemat / penuh | 11 / 40 warung |
| Pelanggan berbayar akhir tahun 1 / 2 / 3 | 17 / 38 / 62 |
| Pendapatan tahun 1 / 2 / 3 | Rp2.868.000 / Rp8.244.000 / Rp14.400.000 |
| Laba bersih tahun 1 / 2 / 3 | -Rp762.966 / Rp2.642.922 / Rp691.200 |
| Kas terendah tahun 1 | Rp5.149.896 (bulan 9) |


*Gambar 4. Warung berbayar akhir bulan, tahun 1.*


*Gambar 5. Saldo kas dan laba bersih bulanan, tahun 1.*


*Gambar 6. Titik impas dibanding ukuran segmen.*

Kesimpulan keuangan: tahap hemat dapat berjalan di dalam segmen awal (11 dari 25 warung), dan modal Rp6.000.000 cukup menahan kerugian tahun 1. Tahap penuh (40 warung) tidak muat di segmen awal, sehingga usaha penuh bergantung pada perluasan ke SWK lain. Tim tidak mengklaim kelayakan komersial penuh sebelum hasil uji harga dan pemakaian tersedia.


*Tabel 17. Skenario tahun 1*

| Skenario | Warung akhir | Laba bersih | Laba positif mulai |
|---|---|---|---|
| Pesimis | 8 | -Rp1.336.032 | Belum tercapai |
| Moderat | 17 | -Rp762.966 | bulan 10 |
| Optimis | 29 | Rp87.498 | bulan 6 |


## Bab 9. Validasi, Uji Pengguna, dan Asumsi Kritis

### 9.1 Asumsi kritis dan ambang keputusan

*Tabel 18. Tiga asumsi kritis (ambang ditetapkan sebelum uji)*

| ID | Rumusan yang dapat diuji | Hasil |
|---|---|---|
| A1 Pendapatan | Minimal 6 dari 10 pemilik warung menyerahkan uang muka Rp10.000 untuk langganan ≥ Rp24.000 per bulan setelah melihat simulasi layar rekap malam | [BELUM DIUJI] |
| A2 Nilai dan pemakaian | Minimal 7 dari 10 pemilik menyelesaikan rekap satu hari dari foto nota atau satu rekaman suara dalam waktu kurang dari 10 menit tanpa bantuan | [BELUM DIUJI] |
| A3 Kanal | Minimal 15 dari 25 pedagang SWK Srikana mendaftar uji coba dalam 14 hari setelah paguyuban memperkenalkan Tumbuh.in | [BELUM DIUJI] |


### 9.2 Rencana uji pengguna prototipe
Pengujian mengikuti format laporan mata kuliah: responden mencoba prototipe lebih dulu, baru mengisi kuesioner. Responden berasal dari segmen target (pemilik atau pelayan warung makan), minimal 5 orang sesuai kriteria UAS dan ditargetkan 8 orang. Target ditetapkan sebelum uji dan hasil dilaporkan apa adanya.


*Tabel 19. Rencana uji*

| Unsur | Isi |
|---|---|
| Tugas 1 | Ambil foto nota (atau rekam suara) dan kirim |
| Tugas 2 | Periksa dan koreksi satu hasil bacaan yang salah |
| Tugas 3 | Baca rekap harian dan sebutkan laba hari itu |
| Tugas 4 | Temukan menu yang hampir habis |
| Ukuran | Keberhasilan tugas, waktu tugas, System Usability Scale (10 butir baku), kuesioner validasi produk, saran terbuka |
| Target (A) | Keberhasilan tugas ≥ 80%; SUS rata-rata ≥ 68 (Sauro, 2011); ≥ 6 dari 10 mau uang muka; rekap < 10 menit |
| Etika | Persetujuan lisan; kode responden R-U1 dst; tanpa data pribadi (UU No. 27/2022) |


*Tabel 20. Hasil uji pengguna*

| Indikator | Target | Hasil |
|---|---|---|
| Jumlah responden segmen target | ≥ 5 (target 8) | [BELUM DIUJI] |
| Keberhasilan tugas | ≥ 80% | [BELUM DIUJI] |
| Skor SUS rata-rata | ≥ 68 | [BELUM DIUJI] |
| Setuju aplikasi membantu masalahnya (skor 4-5) | ≥ 70% | [BELUM DIUJI] |
| Bersedia membayar Rp24.000 per bulan | ≥ 6 dari 10 | [BELUM DIUJI] |

> Hasil di atas sengaja kosong. Tim mengisinya hanya dari data uji nyata dan tidak memakai angka contoh dari template mata kuliah. Hasil akhir dituangkan pada Laporan Uji Pengguna.


## Bab 10. Roadmap dan Kebutuhan

*Tabel 21. Roadmap*

| Fase | Waktu | Kegiatan | Ukuran berhasil |
|---|---|---|---|
| 1. Validasi | Bulan 1-2 | Prototipe Figma, uji pengguna, uang muka A1, ajakan paguyuban A3 | A1 ≥ 6/10; A2 ≥ 7/10; SUS ≥ 68 |
| 2. Pilot | Bulan 3-6 | Bangun versi web sederhana; pendampingan 10 warung | 11 warung berbayar (titik impas tahap hemat) pada bulan 6 |
| 3. Peluncuran terbatas | Bulan 7-12 | Penanda stok; perkiraan belanja bila data cukup; ekspor mingguan | 17 warung berbayar; laba bulanan positif mulai bulan 10 |
| 4. Perluasan | Tahun 2-3 | Perluasan ke SWK lain di Surabaya; pindah ke tahap penuh | Warung berbayar mendekati 40 |


### 10.1 Kebutuhan (ask)
- Akses ke paguyuban pedagang SWK Srikana lewat R-02 (pengurus).
- 10 warung untuk uji uang muka dan pilot (R-02 dan R-04 kandidat, belum ada komitmen).
- Masukan mentor tentang harga dan perluasan.
- Pendanaan: tidak dibutuhkan pada tahap awal karena kas terendah Rp5.149.896. Kebutuhan dana dihitung ulang setelah hasil A1 dan A2.

### 10.2 Risiko utama

*Tabel 22. Risiko*

| Risiko | Penanganan |
|---|---|
| Pemilik tidak mau membayar | Uji uang muka; alternatif harga Rp19.000 atau Alt 2 |
| Akurasi baca foto dan suara rendah | Uji bersama A2; pemilik dapat mengoreksi |
| Paket gratis dijeda atau data hilang | Ekspor mingguan; pindah ke paket Pro |
| Segmen terlalu kecil | Perluas ke SWK lain; tunda tahap penuh |
| Pesaing gratis dengan input foto | Fokus warung makan, suara, stok menu, pendampingan |
| Biaya transport lebih tinggi | Gabungkan kunjungan per sentra; ukur bulan pertama |


## Bab 11. Referensi
Brooke, J. (1996). SUS: A quick and dirty usability scale. Dalam P. W. Jordan dkk. (Ed.), Usability evaluation in industry. Taylor & Francis.

BukuWarung. (2026). BukuWarung Apps for MSMEs [Aplikasi]. Google Play. https://play.google.com/store/apps/details?id=com.bukuwarung (diakses 23 November 2026).

CatatKas. (2026). CatatKas: Buku Kas Keuangan AI [Aplikasi]. Google Play. https://play.google.com/store/apps/details?id=app.catatkas.keuangan (diakses 23 November 2026).

Crunchbase. (2026). BukuKas. https://www.crunchbase.com/organization/bukukas (diakses 23 November 2026).

Dcatat. (2026). Aplikasi Kasir UMKM [Aplikasi]. Google Play. https://play.google.com/store/apps/details?id=com.dcatat.kasir (diakses 23 November 2026).

Dinas Koperasi dan Usaha Mikro Kota Surabaya. (2026). Data pedagang SWK (SIPUMKM Surabaya), dikutip dari Laporan UTS Bab 2.2.

Fitzpatrick, R. (2013). The Mom Test. CreateSpace.

Google. (2026). Harga Gemini API; Bank Indonesia. (2026). Kurs JISDOR 6 Oktober 2026; dikutip dari Laporan UTS Bab 4.4.

Innovecto. (2026). Qasir: Point of Sale & Report [Aplikasi]. Google Play. https://play.google.com/store/apps/details?id=com.innovecto.etalastic (diakses 23 November 2026).

Kelompok 1. (2026). Laporan UTS Business Model Canvas Tumbuh.in. Fakultas Vokasi, Universitas Airlangga.

Midtrans. (2026). Tarif QRIS merchant, dikutip dari Laporan UTS Bab 4.4.

Pemerintah Republik Indonesia. (2022). Peraturan Pemerintah Nomor 55 Tahun 2022 tentang penyesuaian pengaturan di bidang PPh; Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.

Sauro, J. (2011). A practical guide to the System Usability Scale. Measuring Usability LLC.


## Lampiran A. Deklarasi Penggunaan AI
Asisten AI generatif dipakai sebagai alat bantu untuk: menyusun draf business plan dan laporan keuangan dari Laporan UTS Kelompok 1 dan template mata kuliah; mengisi dan menghitung ulang model Excel; membuat grafik; dan mencari daftar pesaing awal. Substansi analisis, angka, dan asumsi menjadi tanggung jawab tim, yang memeriksa ulang angka terhadap file Excel dan sumber UTS. Angka pesaing dan harga yang tidak terverifikasi tidak dicantumkan.


## Lampiran B. Hal Yang Wajib Diisi Tim Sebelum Pengumpulan
- Tautan prototipe Figma (Bab 3.3).
- Nama penanggung jawab tiap peran (Bab 5.3).
- Hasil uji pengguna dan A1 (Bab 9) dari data nyata.
- Pemeriksaan ejaan nama anggota (Alfiyan atau Alfian).
- Tanggal pengumpulan LMS (paling lambat 1 hari sebelum UAS pukul 23.59 WIB).