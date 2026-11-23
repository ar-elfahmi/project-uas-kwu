# 04. Spesifikasi Prototipe Figma (T4)

Untuk dibangun manusia di Figma (H2). Semua data di layar berlabel **"data contoh"**. Tidak ada AI sungguhan dan tidak ada backend (aturan K9).

## Pengaturan umum
- Frame: Android 360 x 800 (satu kolom, mudah dibaca di ponsel pemilik warung).
- Warna: hijau `#2E8B57` (aksi utama), biru tua `#1F3A5F` (judul), oranye `#E8892B` (peringatan stok), latar `#F3F6FA`.
- Font: Inter atau Roboto; isi minimal 16 px; tombol minimal 48 px tinggi (jari berminyak, tangan sibuk).
- Bahasa: Indonesia sehari-hari, kalimat pendek. Tidak ada istilah teknis di layar.
- Prototype: tipe "Click-through"; semua tombol tersambung (Smart animate 200 ms).
- Berbagi: ubah akses ke "Anyone with the link can view", salin tautan ke business plan Bab 3.3 dan deck slide 5.

## Layar 1. Ambil nota
| Elemen | Isi |
|---|---|
| Judul | "Catat hari ini" |
| Tombol besar 1 | Ikon kamera + "Foto nota" |
| Tombol besar 2 | Ikon mikrofon + "Rekam suara" |
| Teks bantu | "Cukup satu nota dulu. Sisanya bisa nanti." |
| Navigasi | Tab bawah: Catat, Rekap, Stok |
| Tautan | "Foto nota" atau "Rekam suara" -> Layar 2 |

## Layar 2. Periksa hasil
| Elemen | Isi (data contoh) |
|---|---|
| Judul | "Sudah terbaca. Cek dulu ya." |
| Daftar | Nasi ayam x 9 = Rp135.000; Es teh x 12 = Rp18.000; Kopi x 5 = Rp25.000 |
| Baris bertanda oranye | "Es teh x 12: benar?" dengan tombol Ubah |
| Tombol | "Betul semua" (hijau) dan "Ubah" |
| Tautan | "Ubah" -> pop-up angka (angka bisa diketuk) lalu kembali; "Betul semua" -> Layar 3 |

## Layar 3. Rekap harian
| Elemen | Isi (data contoh) |
|---|---|
| Judul | "Rekap hari ini" |
| Kartu | Tunai Rp(contoh); QRIS Rp(contoh); Belanja Rp(contoh); **Laba hari ini** Rp(contoh) |
| Info waktu | "Selesai dalam 6 menit" (contoh) |
| Tombol | "Lihat stok" -> Layar 4; "Bagikan lewat WhatsApp" (hanya tampilan) |

## Layar 4. Stok menipis
| Elemen | Isi (data contoh) |
|---|---|
| Judul | "Hampir habis" |
| Daftar | Ayam: sisa sedikit; Es batu: sisa sedikit; Beras: aman |
| Penanda | Titik oranye (menipis), hijau (aman) |
| Teks | "Belanja besok: segera hadir" (fitur lanjutan, tidak berfungsi) |
| Tautan | Tab bawah ke Layar 1 dan 3 |

## Skrip demo 3 sampai 4 menit
| Waktu | Anggota | Aksi di layar | Kalimat kunci |
|---|---|---|---|
| 0:00-0:30 | Pembicara A | Layar 1 | "Bu Ani (nama samaran) baru tutup. Satu nota, satu foto." |
| 0:30-1:30 | Pembicara B | Layar 2, ubah satu angka | "AI bisa salah. Pemilik tinggal koreksi, tidak mengetik ulang." |
| 1:30-2:30 | Pembicara C | Layar 3 | "Laba hari ini langsung terlihat. Dulu 60 sampai 90 menit." |
| 2:30-3:30 | Pembicara D | Layar 4 | "Ayam hampir habis. Besok belanja lebih tepat." |
| 3:30-4:00 | Pembicara A | Kembali ke slide | "Ini data contoh. Akurasi AI kami uji berikutnya (A2)." |

## Cadangan bila Figma gagal terbuka
Siapkan video rekaman layar 60 detik dan tangkapan tiap layar di slide cadangan. Waktu persiapan UAS hanya 2 menit.

## Daftar periksa selesai
- [ ] 4 layar tersambung, bisa diklik dari awal sampai akhir tanpa jalan buntu
- [ ] Semua angka berlabel "data contoh"
- [ ] Tautan "view only" diuji dari akun lain
- [ ] Waktu demo tercatat ≤ 4 menit
