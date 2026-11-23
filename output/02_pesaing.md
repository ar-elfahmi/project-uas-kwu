# 02. Riset Pesaing (T2)

Diakses 23 November 2026 lewat pencarian web. Hanya deskripsi publik toko aplikasi dan situs resmi yang dipakai. Harga paket berbayar **belum diverifikasi**, jadi tidak ditulis. Tim perlu membuka aplikasi sendiri sebelum UAS untuk memastikan fitur dan harga.

| Pesaing | Yang ditawarkan (menurut deskripsi publik) | Fitur foto/suara | Fitur stok | Celah untuk warung makan | Sumber |
|---|---|---|---|---|---|
| BukuWarung | Pembukuan digital, tagihan, QRIS, produk digital, pembiayaan; platform gratis untuk UMKM | Tidak disebut | Tidak disebut | Fokus luas (agen pembayaran, pulsa). Catat transaksi manual | [Google Play](https://play.google.com/store/apps/details?id=com.bukuwarung), [bukuwarung.com](https://www.bukuwarung.com/career/) |
| BukuKas | Pembukuan UMKM: catat transaksi, laporan otomatis, kelola stok barang | Tidak disebut | Ya | Input manual per transaksi | [Crunchbase](https://www.crunchbase.com/organization/bukukas) |
| Qasir | Aplikasi kasir (POS) dengan fitur dasar gratis dan laporan penjualan | Tidak disebut | Ya (POS) | Input per pesanan; jenis alat yang ditinggalkan R-04 | [Google Play](https://play.google.com/store/apps/details?id=com.innovecto.etalastic) |
| CatatKas | Buku kas; catat dari foto struk atau ketik seperti chat | **Ya (foto struk)** | Tidak disebut | Paling mirip. Deskripsi menyebut pribadi, keluarga, RT, masjid; stok menu warung tidak disebut | [Google Play](https://play.google.com/store/apps/details?id=app.catatkas.keuangan) |
| Dcatat Kasir | Kasir gratis, catat penjualan, stok, bekerja offline | Tidak disebut | Ya | Input per penjualan | [Google Play](https://play.google.com/store/apps/details?id=com.dcatat.kasir) |

## Peta posisi (dua sumbu)
Sumbu X: kemudahan input (kiri = input per transaksi, kanan = cukup catat sekali). Sumbu Y: kedalaman fitur untuk warung makan (stok menu, rekap harian).

```
 Y tinggi |  Qasir        BukuKas           [Tumbuh.in: target]
          |  Dcatat
          |  BukuWarung               CatatKas
 Y rendah |
          +--------------------------------------------------
            input per transaksi                catat sekali  (X)
```
Penempatan ini penilaian tim dari deskripsi publik, bukan hasil uji aplikasi.

## Kesimpulan jujur
1. Input foto nota sudah ada di CatatKas. Klaim "pertama" tidak boleh dipakai.
2. Pembeda yang masih bisa dipertahankan: fokus warung makan, satu rekaman suara, penanda stok menu, dan pendampingan hari pertama. Semuanya belum diuji.
3. Pesaing gratis menekan harga. Rp24.000/bulan perlu dibenarkan lewat waktu rekap yang jauh lebih singkat.
4. Tutup uji #2 UTS ("penggantian nama") hanya sebagian: fitur pesaing sudah dibandingkan secara tertulis, tetapi belum dicoba langsung.
