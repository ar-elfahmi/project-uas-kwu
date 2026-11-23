# LOG Pengerjaan UAS Tumbuh.in

Tanggal kerja: 23 November 2026. Skrip pembuat file ada di `tools/`.

## Luaran akhir (dikumpulkan)
| File | Status |
|---|---|
| `Lampiran_Keuangan_Tumbuh-in.xlsx` | Selesai; 8/8 cek OK |
| `Laporan_Keuangan_Tumbuh-in.docx` | Selesai |
| `Pitch_Deck_Tumbuh-in.pdf` | Selesai; slide 5 dan 6 perlu pembaruan (Figma, hasil uji) |
| `Business_Plan_Tumbuh-in.docx` | Selesai; perlu tautan Figma, nama peran, hasil uji |
| Laporan uji pengguna (PDF) | **Belum**: kerangka di `06_laporan_uji.md`, tunggu data lapangan |
| Prototipe (tautan) | **Belum**: spesifikasi di `04_spec_prototipe.md` |

## Berkas pendukung (tugas master brief)
| Tugas | Berkas | Status |
|---|---|---|
| T1 | `00_fakta.md` | Selesai |
| T2 | `02_pesaing.md` | Selesai (harga paket pesaing belum diverifikasi) |
| T3 | `Lampiran_Keuangan_Tumbuh-in.xlsx`, `03_ringkasan_keuangan.md` | Selesai |
| T4 | `04_spec_prototipe.md` | Selesai; dibangun manusia di Figma |
| T5 | `05_rencana_uji.md`, `05_form_rekap_uji.xlsx` | Selesai |
| T6 | `06_laporan_uji.md` | Kerangka; menunggu data nyata |
| T7 | `07_pemasaran.md` | Selesai |
| T8 | `08_business_plan.md` (teks), `Business_Plan_Tumbuh-in.docx` | Selesai |
| T9 | `09_deck_outline.md`, `Pitch_Deck_Tumbuh-in.pdf` | Selesai |
| T10 | `10_skrip_dan_qna.md` | Selesai |
| T11 | `11_qa_dan_deklarasi_ai.md` | Selesai |

## Perubahan dari sumber (K5)
1. Pendampingan Rp30.000 dipindah dari variabel ke CAC. BEP UTS 12 dan 46 menjadi 11 dan 40. Alasan: hindari hitung ganda; template UAS punya baris CAC.
2. Biaya penagihan QRIS dihitung 0,7% x Rp24.000 = Rp168 (UTS memakai Rp150 dibulatkan).
3. Tahun 2 tetap tahap hemat (Rp171.000); tahun 3 tahap penuh (Rp663.000), mengikuti pemicu UTS (mendekati 40-46 warung).

## Keputusan asumsi baru (semua A)
Churn 5% / 4,5% / 4%; warung baru 2 / 3 / 4 per bulan; modal Rp6.000.000; honor, perangkat, MVP, legalitas Rp0; CAC Rp30.000.

## Hal yang butuh manusia
Tautan Figma; uji lapangan dan A1; nama peran; ejaan nama anggota; tanggal UAS; bobot rubrik; verifikasi fitur dan harga pesaing; cek tampilan file Word.

## Batas pengecekan
File Word belum dirender menjadi halaman (tidak ada Word/LibreOffice). Excel tidak menyimpan hasil hitung sampai dibuka di Excel; angka diverifikasi dengan pustaka `formulas` (Python).
