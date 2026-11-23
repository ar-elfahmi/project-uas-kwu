# 11. QA Akhir dan Deklarasi AI (T11)

## Hasil pemeriksaan otomatis (dijalankan saat pembuatan)
| Pemeriksaan | Hasil |
|---|---|
| Rumus Excel sama dengan template (semua sheet) | Lolos, 0 rumus berubah |
| `Cek_Konsistensi` Excel | 8 dari 8 OK; jumlah CEK = 0 |
| Angka laporan keuangan, business plan, deck = hasil hitung Excel | Lolos (dibangkitkan dari satu sumber hitung) |
| Sisa kata contoh "StokMudah", "Tim 3", "149.000" di dokumen akhir | Tidak ada |
| Deck ≤ 15 slide utama, 9 bagian berurutan | Lolos (15 + 4 lampiran) |
| Slide terakhir memuat referensi dan deklarasi AI | Lolos |
| Form rekap uji (`05_form_rekap_uji.xlsx`) | Rumus SUS diuji dengan data dummy di salinan terpisah (hasil cocok dengan hitungan manual); file akhir kosong |

## Daftar periksa Bagian 8 master brief
| Butir | Status | Catatan |
|---|---|---|
| 5 luaran wajib ada | **Belum penuh** | Laporan uji pengguna masih kerangka; tautan Figma belum ada |
| Deck ≤ 15 slide, 9 bagian, slide akhir deklarasi AI | Ya | |
| Semua anggota punya bagian bicara dan Q&A | Ya | Usulan di `10_skrip_dan_qna.md` |
| `Cek_Konsistensi` OK dan tidak ada rumus diganti angka | Ya | |
| Tidak ada sisa "StokMudah", "Tim 3", "149.000" | Ya | Dua kata "freelancer" dan "rekaan" di xlsx adalah catatan bantu, bukan contoh |
| Tidak ada hasil uji karangan | Ya | Semua `[BELUM DIUJI]` |
| Setiap angka penting punya sumber atau tanda A | Ya | |
| Tidak ada klaim layak komersial tanpa bukti | Ya | |
| Nama responden tidak muncul | Ya | |
| Unggah LMS sebelum H-1 23.59 WIB | Menunggu tim | Tanggal UAS belum diketahui |

## Hal yang masih harus dikerjakan manusia
1. Bangun prototipe Figma dan masukkan tautan (business plan Bab 3.3, deck slide 5).
2. Uji lapangan 5 sampai 8 responden dan uji uang muka (A1); isi `05_form_rekap_uji.xlsx`.
3. Isi `06_laporan_uji.md`, ekspor PDF; perbarui slide 6 dan Bab 9 business plan dengan hasil nyata.
4. Nama penanggung jawab peran (business plan Bab 5.3) dan ejaan nama anggota (Alfiyan atau Alfian).
5. Buka kedua file `.docx` di Word; pilih Yes untuk memperbarui daftar isi. Buka file Excel di Excel agar rumus terhitung.
6. Cek rubrik penilaian dari dosen (PDF kriteria tidak memuat bobot nilai).
7. Buka aplikasi pesaing sendiri dan pastikan fitur dan harga di `02_pesaing.md`.
8. Pastikan pajak dan bentuk usaha (PPh final 0,5% dipakai konservatif dari template).

## Batas pengecekan
Dokumen Word belum dirender sebagai halaman karena tidak ada Word atau LibreOffice di komputer pembuat. Strukturnya diperiksa lewat kode; deck PDF dilihat sebagai gambar halaman. Periksa tampilan dokumen Word sebelum dikumpulkan.

## Deklarasi penggunaan AI (siap ditempel)
> Asisten AI generatif (Kiro, model dipilih otomatis oleh platform) dipakai sebagai alat bantu untuk: (1) menyusun draf business plan, laporan keuangan, pitch deck, skrip, dan bank tanya jawab dari Laporan UTS Kelompok 1 dan template mata kuliah; (2) mengisi template Excel dan menghitung ulang model keuangan; (3) membuat grafik; (4) mencari daftar pesaing awal lewat pencarian web (diakses 23 November 2026). Substansi analisis, asumsi, dan seluruh angka menjadi tanggung jawab tim. Tim memeriksa ulang angka terhadap file Excel dan sumber UTS. Data wawancara dan hasil uji pengguna berasal dari pengumpulan lapangan tim, bukan dari AI. Angka pesaing yang tidak terverifikasi tidak dicantumkan.

Tempel di slide terakhir (sudah ada versi singkat di slide 15) dan di Lampiran A business plan. Ganti nama model bila tim memakai alat lain.
