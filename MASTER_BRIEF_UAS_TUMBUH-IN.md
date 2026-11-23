# MASTER BRIEF: UAS Kewirausahaan Bidang TI, Tumbuh.in

Brief ini berdiri sendiri. Tempel seluruh isinya ke agen AI mana pun (Claude, Codex, Gemini, Copilot, Cursor, Kiro). Lalu minta: "Kerjakan tugas T<n>". Kerjakan satu tugas per sesi.

## 0. Cara memakai

1. Berikan agen akses ke folder proyek ini.
2. Tempel brief ini. Sebut satu nomor tugas (Bagian 6).
3. Agen menulis hasil ke `output/` (Bagian 7). Jangan menimpa file sumber.
4. Setelah selesai, agen mengisi `output/LOG.md` (apa dibuat, apa belum, apa butuh manusia).

Bahasa semua keluaran: Indonesia, sederhana, kalimat pendek.

## 1. Konteks

- Mata kuliah: Kewirausahaan Bidang TI (FVK25612002), D4 Teknik Informatika, Fakultas Vokasi, Universitas Airlangga. Gasal 2026/2027. Dosen: Nambi Sembilu, S.Kom., M.Kom.
- Tim: Kelompok 1, 6 anggota. Alung Destantio Cahya Utama Putra (434241001), Daffa Eka Sujianto (434241004), Muhammad Javier Rakha Abhista (434241021), Nabil Hakim Alfikri (434241055), Alfiyan Rasyid El-Fahmi (434241047), Muhammad Reyhan Ammar (434241061). Ejaan "Alfiyan/Alfian" belum pasti (H4).
- Ujian: presentasi proyek akhir tim + demo prototipe + tanya jawab individual. Total sekitar 28 menit: persiapan 2, presentasi+demo 12 (demo 3 sampai 4), tanya jawab 12 (min. 2 pertanyaan per anggota, termasuk 1 lintas bagian), penilaian 2.
- Semua anggota wajib hadir dan berbicara.
- Pengumpulan: LMS, paling lambat 1 hari sebelum UAS pukul 23.59 WIB. Tanggal UAS belum diketahui (H1).

## 2. Sumber kebenaran (urutan menang)

| # | File di folder proyek | Peran |
|---|---|---|
| 1 | `Kriteria_UAS_Presentasi_Proyek_Akhir_Kewirausahaan_TI (2).pdf` | Aturan: luaran dan struktur presentasi |
| 2 | `UTS_KWU-TI_Tim1_Tumbuh-in-AI FINAL.md` | Fakta produk, wawancara, BMC, biaya, titik impas. File besar karena gambar base64: baca per bagian, jangan seluruhnya |
| 3 | `Format_Laporan_Hasil_Pengujian_dan_Form_Pengujian.docx` | Bentuk laporan uji (Bab 1 sampai 8, Form 1 sampai 3) |
| 3 | `Salinan dari Format_Laporan_Keuangan_Proyek_Usaha_Digital.xlsx` | Bentuk model keuangan (sheet Asumsi, Unit_Economics, Proyeksi_Bulanan, Laba_Rugi, Arus_Kas, Neraca, Tahun2_3, Ringkasan_3Thn, Sensitivitas, Cek_Konsistensi) |
| 4 | `UTS_KWU-TI_Tim1_Tumbuh-in-AI Pichdeck.pdf` | Gaya deck UTS |

Peringkat 3 berisi contoh fiktif usaha "StokMudah". Pakai bentuknya saja.

## 3. Aturan keras

- K1. Dilarang mengarang data. Hasil uji pengguna, kutipan wawancara, angka pasar, dan harga pesaing harus berasal dari sumber nyata. Belum ada → tulis `[BELUM DIUJI]` atau `[ISI DARI LAPANGAN]`.
- K2. Setiap angka penting punya sumber, atau diberi tanda A (asumsi). Pakai penanda UTS: F (fakta, kode R-01..R-04), S (sumber luar, tulis sumber dan tanggal), A (asumsi tim).
- K3. Jangan menyalin nilai contoh template: "StokMudah", "Tim 3", Rp149.000, 12 responden, SUS 70,6, 92%, dsb. Sebelum selesai, cari kata-kata itu dan hapus.
- K4. Lampiran keuangan memakai rumus. Jangan mengetik hasil. Semua status di `Cek_Konsistensi` harus OK.
- K5. Nilai tetap dari UTS. Bila perlu mengubah, catat di `output/LOG.md` dengan alasan.
- K6. Jangan klaim "layak komersial". Bukti baru: 4 wawancara masalah (3 di satu sentra). Kesediaan membayar dan akurasi AI belum terbukti.
- K7. Penggunaan AI wajib dideklarasikan di slide terakhir dan lampiran laporan (tugas T11).
- K8. Nama dan usaha responden tidak ditulis. Pakai kode R-01..R-04 (UU PDP No. 27/2022).
- K9. Jangan membangun hal di luar daftar. Tidak ada aplikasi sungguhan, tidak ada backend.

## 4. Fakta kanonik (ringkasan UTS)

**Produk.** Tumbuh.in: aplikasi web ringan. Pemilik warung memotret nota atau merekam satu pesan suara saat senggang. Aplikasi menyusun rekap harian (tunai + QRIS), penanda stok menipis, lalu perkiraan belanja besok (fitur lanjutan, menyusul). Pemilik boleh mengoreksi hasil. Target rekap di bawah 10 menit (A, belum diuji).

**Masalah.** Pemilik warung makan dan kedai kecil sekitar kampus. Setelah tutup: rekap uang 60 sampai 90 menit/hari (R-02 sekitar 60, R-04 sekitar 90), atau tidak mencatat dan laba ditebak (R-01, R-03). Saat jualan: stok tak terlihat. 3 dari 4 pernah kehabisan menu/bahan (R-01, R-02, R-04). n = 4, wawancara 13 Oktober 2026.

**Sasaran (dilayani):** H1 rekap, H2 stok, H3 cepat dan mudah (POS lama R-04 ditinggalkan). **Tidak dilayani:** H4 makanan terbuang, H5 rekonsiliasi QRIS.

**Kutipan verbatim yang boleh dipakai.**
- R-01 00:54: "Gak ate dicatet wes. Gak ate dicatet, apa dicatet."
- R-02 14:15: "Wis... satu jam lah."
- R-02 04:30: "Pernah, sering."
- R-04 02:44: "Soalnya kita tidak bisa melihat barang menu yang stoknya tinggal berapa dan untuk betulnya berapa."
- R-04 07:00: pernah mencoba POS, bermasalah dan penjualan jadi lebih lama, kembali ke buku.

**Segmen.** Awal: 25 pedagang SWK Srikana (SIPUMKM Surabaya). Batas atas 58 bila SWK Mulyorejo ikut (hanya untuk uji titik impas). Pengguna awal: R-04, R-02. Pengguna = pemilik/pelayan; pembayar dan pengambil keputusan = pemilik (A, belum ditanyakan). Paguyuban = perekomendasi, bukan pembayar.

**Pernyataan nilai.** Untuk pemilik warung makan dan kedai kecil di sekitar kampus yang tiap malam menghabiskan 60 sampai 90 menit merekap uang atau tidak tahu laba harian dan menu yang hampir habis, Tumbuh.in memberikan rekap harian tunai dan QRIS dari foto nota atau satu rekaman suara, disertai penanda stok, target rekap di bawah 10 menit. Beda dari buku tulis dan aplikasi kasir yang menuntut input tiap pesanan.

**Model bisnis.** Kanal: kunjungan langsung ke sentra, rekomendasi paguyuban, demo dengan nota milik sendiri, web tanpa instal, WhatsApp purna jual. Hubungan: pendampingan hari pertama, lalu swalayan satu layar. Pendapatan: Alt 1 langganan Rp24.000/warung/bln (uji di Rp29.000, 24.000, 19.000); Alt 2 per pemakaian Rp1.000 per rekap (cadangan). Alt 3 freemium gugur. Kemitraan: penyedia AI/hosting, paguyuban, warung pilot (R-02, R-04 kandidat), penyedia QRIS.

**Biaya (UTS Bab 4.4).**

| Item | Nilai UTS |
|---|---|
| Biaya tetap tahap hemat | Rp171.000/bln (Supabase gratis, Cloudflare Pages gratis, domain Rp5.000, paket data+transport Rp150.000, cadangan 10%) |
| Biaya tetap tahap penuh | Rp663.000/bln (+ Supabase Pro Rp448.000). Pesimis Rp994.000 |
| Variabel UTS | Rp9.550 = AI Rp6.900 + pendampingan Rp2.500 + penagihan Rp150 |
| Kurs | Rp17.917/US$ (JISDOR 6 Okt 2026). Model Gemini 3.5 Flash-Lite |
| BEP UTS Alt 1 | 12 warung (hemat), 46 (penuh) |
| BEP UTS Alt 2 | 14 (hemat), 54 (penuh) |
| Pemicu tahap penuh | ±46 warung berbayar atau basis data > 400 MB |

**Koreksi UAS (keputusan D8, D9).** Template punya baris CAC terpisah. Pindahkan pendampingan Rp30.000 ke CAC. Variabel jadi ±Rp7.068 (AI 6.900 + penagihan 0,7% x 24.000 = 168). Margin ±Rp16.932. BEP ±11 (hemat) dan ±40 (penuh). Hitung ulang dengan rumus; catat selisih dari UTS di laporan.

**Asumsi kritis & ambang (UTS Bab 4.3).**
- A1: ≥6 dari 10 pemilik menyerahkan uang muka Rp10.000 (titipan) untuk langganan ≥Rp24.000/bln setelah melihat simulasi.
- A2: ≥7 dari 10 menyelesaikan rekap satu hari dari foto/suara dalam <10 menit tanpa bantuan.
- A3: ≥15 dari 25 pedagang SWK Srikana mendaftar uji coba dalam 14 hari lewat paguyuban.

**Keputusan lain.** Dana awal: modal tim Rp6.000.000 (A), tanpa investor, tanpa honor. Prototipe: Figma klik-tembus 4 layar. Kanal digital: WhatsApp Business utama, Instagram/TikTok demo pendek sekunder.

## 5. Luaran wajib (dari kriteria UAS)

| Luaran | Isi minimum | Format |
|---|---|---|
| Business plan final | Ringkasan eksekutif, masalah & validasi, solusi, model bisnis, operasional, pemasaran, keuangan, roadmap, referensi | PDF |
| Lampiran keuangan | Harga pokok layanan, BEP, arus kas 12 bulan, CAC/LTV; pakai rumus | .xlsx |
| Pitch deck | Maks 15 slide utama + lampiran, urutan Bagian 5 | PPTX/PDF |
| Prototipe | Tautan Figma/aplikasi | Tautan |
| Laporan uji pengguna | Rencana uji, profil ≥5 pengguna target, tugas, hasil (keberhasilan tugas/SUS), temuan, perbaikan | PDF |

**Urutan presentasi / pitch deck.**
1. Masalah dan bukti validasi (customer discovery)
2. Solusi dan value proposition
3. Demo prototipe dan hasil uji pengguna
4. Model bisnis dan rencana operasional
5. Strategi pemasaran: STP, positioning statement, 7P, harga, pesaing
6. Kanal digital, kalender konten, KPI kampanye
7. Keuangan: harga pokok layanan, BEP, arus kas, unit economics
8. Tim, roadmap, kebutuhan (ask)
9. Referensi dan deklarasi penggunaan AI

Catatan: PDF kriteria tidak memuat tabel bobot nilai (H3). Jangan menebak bobot.

## 6. Daftar tugas

Tiap tugas: Masukan, Kerjakan, Selesai bila. Kerjakan sesuai urutan ketergantungan.

### T1. Fakta kanonik (tanpa ketergantungan)
- Masukan: UTS .md (bagian Bab 1 sampai 4, Lampiran A).
- Kerjakan: salin Bagian 4 brief ini ke `output/00_fakta.md`, verifikasi tiap angka dan kutipan terhadap UTS. Tandai selisih.
- Selesai bila: tiap angka ada rujukan bab UTS; selisih tercatat.

### T2. Riset pesaing (butuh T1)
- Kerjakan: cari 4 sampai 5 pesaing nyata di Indonesia untuk pencatatan keuangan/kasir UMKM warung (contoh yang dicek: BukuWarung, BukuKas, Qasir, Moka POS, Olsera; verifikasi bahwa masih ada). Per pesaing: harga, fitur foto/suara/stok, kelemahan terhadap segmen, URL, tanggal akses.
- Keluaran: `output/02_pesaing.md` (tabel + peta posisi 2 sumbu: kemudahan input vs kedalaman fitur).
- Selesai bila: semua angka punya URL dan tanggal; tabel jujur bila fitur pesaing sebanding. Menutup uji #2 UTS.

### T3. Model keuangan (butuh T1)
- Masukan: file xlsx template. Salin ke `output/Lampiran_Keuangan_Tumbuh-in.xlsx`, jangan edit asli.
- Kerjakan: isi sheet `Asumsi` saja (sel biru/kuning), kolom D wajib sumber. Ganti semua nama StokMudah. Nilai: harga Rp24.000; churn 5% (A); CAC Rp30.000; cloud Rp0; WhatsApp Rp0; payment gateway 0,7%; biaya tetap tahap hemat Rp171.000 diurai per pos UTS; modal pendiri Rp6.000.000; investor Rp0; perangkat Rp0; MVP Rp0; honor Rp0. Pelanggan baru per bulan: naik bertahap, kumulatif tahun 1 tidak melebihi 25 (skenario optimis boleh sampai 58). Skenario pesimis/moderat/optimis di `Sensitivitas`.
- Selesai bila: `Cek_Konsistensi` semua OK; tidak ada angka hasil yang diketik; BEP tercatat; kas terendah tidak negatif (bila negatif, laporkan jujur dan sarankan tambahan modal).
- Keluaran tambahan: `output/03_ringkasan_keuangan.md` (BEP, LTV, CAC payback, kas terendah, perbandingan dengan UTS).

### T4. Spesifikasi prototipe (butuh T1)
- Kerjakan: spesifikasi Figma untuk 4 layar. L1 Ambil foto nota / rekam suara. L2 Cek dan koreksi hasil bacaan. L3 Rekap harian (tunai, QRIS, laba, durasi). L4 Penanda stok menipis. Isi tiap layar: elemen, teks, data contoh (berlabel "data contoh"), tautan antar layar. Tambah skrip demo 3 sampai 4 menit.
- Keluaran: `output/04_spec_prototipe.md`.
- Selesai bila: manusia bisa membangunnya di Figma tanpa bertanya lagi. Dibangun oleh manusia (H2).

### T5. Instrumen uji pengguna (butuh T4)
- Kerjakan: rencana uji dengan 4 tugas (ambil foto nota, koreksi hasil, baca rekap, temukan menu hampir habis). Form 1 (profil, SUS 10 butir baku tanpa ubah, validasi produk) dan form rekap Form 2 dan 3 dalam spreadsheet berumus (skor SUS: ganjil−1, genap 5−skor, jumlah x 2,5). Target ditetapkan sebelum uji: SUS ≥68, keberhasilan tugas ≥80%, ≥6 dari 10 mau uang muka (A1), rekap <10 menit (A2). Responden target 8, minimal 5, dari segmen. Persetujuan lisan, kode R-U1.., tanpa data pribadi.
- Keluaran: `output/05_rencana_uji.md`, `output/05_form_rekap_uji.xlsx`.
- Selesai bila: sisa pekerjaan hanya mengumpulkan jawaban lapangan.

### T6. Laporan uji pengguna (butuh data lapangan H6)
- Masukan: jawaban uji nyata. Bentuk: docx template (Bab 1 sampai 8).
- Kerjakan: isi laporan dari data nyata. Laporkan hasil apa adanya, termasuk yang gagal. Jika data belum ada, hasilkan kerangka dengan `[BELUM DIUJI]`.
- Keluaran: `output/06_laporan_uji.md` (lalu diekspor ke PDF).
- Selesai bila: tiap angka bisa ditelusuri ke baris rekap. Dilarang memakai contoh StokMudah.

### T7. Pemasaran (butuh T1, T2)
- Kerjakan: STP (segmen, target, positioning statement 1 kalimat), 7P (product, price, place, promotion, people, process, physical evidence) dengan harga Rp24.000, kanal digital, kalender konten 4 minggu (3 unggahan per minggu, WhatsApp Business + Instagram/TikTok demo pendek), KPI kampanye (permintaan demo, daftar uji coba terhadap target A3 15 dari 25, uang muka terhadap A1, aktivasi rekap <10 menit, retensi mingguan). Target KPI diberi tanda A.
- Keluaran: `output/07_pemasaran.md`.

### T8. Business plan PDF (butuh T3, T6, T7)
- Kerangka: Ringkasan eksekutif; Masalah & validasi; Solusi; Model bisnis (BMC); Operasional (alur harian, tim, pendampingan, pemicu pindah ke tahap penuh); Pemasaran (dari T7); Keuangan (dari T3); Roadmap (3 fase: uji A1-A3, pilot 5 sampai 10 warung, perluasan SWK lain); Tim dan kebutuhan (ask); Referensi; Lampiran deklarasi AI.
- Ask (A): akses paguyuban, 10 warung pilot, mentor. Bila meminta dana, tulis jumlah berdasarkan kas terendah T3.
- Keluaran: `output/08_business_plan.md` (lalu PDF, ukuran bab proporsional, ≤25 halaman).
- Selesai bila: tiap angka punya F/S/A; konsisten dengan xlsx.

### T9. Pitch deck (butuh T8)
- Kerjakan: ≤15 slide utama mengikuti 9 bagian Bagian 5 + lampiran. Satu pesan per slide, teks sedikit. Slide 3 memuat tangkapan demo dan hasil uji (nyata saja). Slide terakhir: referensi dan deklarasi AI.
- Keluaran: `output/09_deck_outline.md` (judul, isi, catatan pembicara, penanda anggota). Bila agen bisa membuat file: `output/09_deck.pptx`.

### T10. Skrip dan tanya jawab (butuh T9)
- Kerjakan: skrip 12 menit (demo 3 sampai 4 menit), bagi 6 anggota dengan waktu tiap orang. Bank 24 pertanyaan (≥2 per anggota termasuk 1 lintas bagian) dengan jawaban jujur, termasuk pertanyaan sulit: "Mengapa tidak layak di tahap penuh?", "Apa bukti orang mau bayar?", "Bagaimana akurasi AI?", "Beda dari BukuWarung?".
- Keluaran: `output/10_skrip_dan_qna.md`.

### T11. QA akhir (butuh semua)
- Kerjakan: periksa daftar Bagian 8. Tulis deklarasi AI (alat apa, untuk apa, bagian mana, siapa yang memverifikasi). Cari sisa kata contoh (K3). Cek ejaan nama.
- Keluaran: `output/11_qa_dan_deklarasi_ai.md`.

## 7. Struktur folder keluaran

```
project-uas-kwu/
  output/
    LOG.md
    00_fakta.md
    02_pesaing.md
    Lampiran_Keuangan_Tumbuh-in.xlsx
    03_ringkasan_keuangan.md
    04_spec_prototipe.md
    05_rencana_uji.md
    05_form_rekap_uji.xlsx
    06_laporan_uji.md
    07_pemasaran.md
    08_business_plan.md
    09_deck_outline.md
    10_skrip_dan_qna.md
    11_qa_dan_deklarasi_ai.md
```

## 8. Daftar periksa akhir

- [ ] 5 luaran wajib ada (business plan PDF, xlsx, deck, tautan prototipe, laporan uji PDF)
- [ ] Deck ≤15 slide utama; 9 bagian berurutan; slide terakhir deklarasi AI
- [ ] Semua anggota punya bagian bicara dan jawaban Q&A
- [ ] `Cek_Konsistensi` OK; tidak ada rumus diganti angka
- [ ] Tidak ada "StokMudah", "Tim 3", "149.000" tersisa
- [ ] Tidak ada hasil uji karangan; semua angka uji ada baris rekapnya
- [ ] Setiap angka penting: sumber atau tanda A
- [ ] Tidak ada klaim "layak komersial" tanpa bukti
- [ ] Nama responden tidak muncul
- [ ] Unggah LMS sebelum H-1 23.59 WIB

## 9. Butuh manusia

| # | Butir |
|---|---|
| H1 | Tanggal UAS dan batas LMS |
| H2 | Bangun prototipe di Figma dan bagikan tautan |
| H3 | Cek bobot nilai bila dosen punya rubrik lengkap |
| H4 | Pastikan ejaan nama |
| H5 | Bagi peran bicara dan latihan |
| H6 | Uji pengguna di lapangan, kumpulkan jawaban |
| H7 | Jalankan eksperimen A1 (uang muka) bila ingin klaim bukti membayar |

## 10. Urutan yang disarankan

T1 → (T2, T3, T4 bergantian) → T5 → H2 → H6 → T6 → T7 → T8 → T9 → T10 → T11 → unggah.

Memori komputer terbatas: jalankan satu agen pada satu waktu.
