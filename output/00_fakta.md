# 00. Fakta Kanonik Tumbuh.in (T1)

Sumber: Laporan UTS Kelompok 1 (`UTS_KWU-TI_Tim1_Tumbuh-in-AI FINAL.md`). Setiap butir diberi rujukan bab UTS. Tanda: F = fakta wawancara, S = sumber luar, A = asumsi tim.

## 1. Produk
Aplikasi web ringan. Pemilik warung memotret nota atau merekam satu pesan suara saat senggang. Aplikasi menyusun rekap harian (tunai + QRIS) dan penanda stok. Pemilik boleh mengoreksi hasil. Perkiraan belanja besok adalah fitur lanjutan. Target rekap < 10 menit = A, belum diuji. (UTS Bab 2.7)

## 2. Masalah (F, n = 4, wawancara 13 Oktober 2026)
| Butir | Nilai | Responden | UTS |
|---|---|---|---|
| Rekap/laba menjadi hambatan | 4 dari 4 | R-01 sampai R-04 | Bab 1.2 |
| Waktu rekap | ±60 menit (R-02), ±90 menit (R-04) | R-02, R-04 | Bab 1.2 |
| Tidak mencatat, laba ditebak | 2 dari 4 | R-01, R-03 | Bab 1.3 |
| Pernah kehabisan menu/bahan | 3 dari 4 | R-01, R-02, R-04 (R-03 tersirat) | Bab 1.2 |
| Alat lama ditinggalkan | POS dicoba lalu berhenti | R-04 | Bab 1.3 |

Kutipan verbatim yang boleh dipakai: R-01 00:54 ("Gak ate dicatet wes. Gak ate dicatet, apa dicatet."); R-02 14:15 ("Wis... satu jam lah."); R-02 04:30 ("Pernah, sering."); R-04 02:44 (stok tidak terlihat); R-04 07:00 (POS bermasalah, kembali ke buku). (Bab 1.4)

## 3. Segmen
- Segmen awal: 25 pedagang SWK Srikana (S, SIPUMKM Surabaya). Batas atas 58 bila SWK Mulyorejo ikut, hanya untuk uji titik impas. (Bab 2.2)
- Subsegmen A: sudah mencatat manual (R-02, R-04). B: belum mencatat (R-01, R-03). (Bab 2.1)
- Pengguna: pemilik atau pelayan (F). Pembayar dan pengambil keputusan: pemilik (A, belum ditanyakan). Paguyuban: perekomendasi saja. (Bab 2.4)
- Hambatan yang dilayani: H1 rekap, H2 stok, H3 cepat dan mudah. Tidak dilayani: H4 makanan terbuang, H5 rekonsiliasi QRIS. (Bab 2.6)

## 4. Model bisnis
Kanal: kunjungan langsung, paguyuban, demo dengan nota sendiri, web tanpa instal, WhatsApp. Hubungan: pendampingan hari pertama lalu swalayan. Pendapatan: Alt 1 langganan Rp24.000/bulan (uji di Rp19.000, 24.000, 29.000), Alt 2 Rp1.000 per rekap (cadangan), Alt 3 freemium gugur. Kemitraan: penyedia AI/hosting, paguyuban, warung pilot (R-02, R-04 kandidat), penyedia QRIS. Dari 33 isian kanvas: 7 F, 4 S, 22 A. (Bab 3 dan 4.1)

## 5. Biaya dan titik impas
| Item | UTS (Bab 4.4) | UAS (dipakai di xlsx) |
|---|---|---|
| Biaya tetap hemat | Rp171.000 | Rp171.000 |
| Biaya tetap penuh | Rp663.000 | Rp663.000 |
| Variabel | Rp9.550 (AI 6.900 + pendampingan 2.500 + QRIS 150) | Rp7.068 (AI 6.900 + QRIS 0,7% x 24.000 = 168) |
| CAC | tidak ada | Rp30.000 (pendampingan, dipindah) |
| Margin | Rp14.450 | Rp16.932 |
| BEP Alt 1 hemat / penuh | 12 / 46 | 11 / 40 |
| BEP Alt 2 hemat / penuh | 14 / 54 | 12 / 45 |

Dasar variabel AI: Gemini 3.5 Flash-Lite US$0,30 masuk dan US$2,50 keluar per juta token; kurs JISDOR Rp17.917 (6 Okt 2026); 20 catatan/hari x 26 hari + 4 ringkasan Batch (S/A).

## 6. Asumsi kritis (ambang UTS Bab 4.3)
- A1: ≥ 6 dari 10 pemilik menyerahkan uang muka Rp10.000 untuk langganan ≥ Rp24.000.
- A2: ≥ 7 dari 10 menyelesaikan rekap satu hari dari foto/suara dalam < 10 menit tanpa bantuan.
- A3: ≥ 15 dari 25 pedagang SWK Srikana mendaftar uji coba dalam 14 hari lewat paguyuban.
Status semua: belum diuji.

## 7. Selisih UTS vs UAS yang disengaja
1. Pendampingan Rp30.000 pindah dari variabel ke CAC (template UAS punya baris CAC). Efek: BEP 12 -> 11 dan 46 -> 40.
2. Penagihan QRIS dihitung 0,7% dari harga (Rp168), bukan Rp150 dibulatkan.
3. Pelanggan baru tahun 1 dibatasi 2 per bulan (total 24, tidak melebihi segmen 25). UTS tidak punya proyeksi bulanan.

## 8. Temuan konsistensi
- Ejaan nama: UTS "Alfiyan Rasyid El-Fahmi", deck UTS "Alfian Rasyid El Fahmi". Perlu keputusan tim.
- Template uji pengguna dan template keuangan berisi contoh fiktif "StokMudah" (Rp149.000, 12 responden, SUS 70,6). Tidak boleh dipakai.
