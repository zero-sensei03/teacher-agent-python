# Laporan Pengujian Prototipe

Tanggal pengujian: 27 Oktober 2026

## Lingkungan
- Bahasa: Python 3.12
- Antarmuka: Streamlit
- Database riwayat: SQLite
- Provider AI: OpenAI dan Google Gemini tersedia melalui konfigurasi

## Hasil pengujian

| ID | Skenario | Hasil |
|---|---|---|
| T01 | Aplikasi Streamlit dapat dijalankan | Lulus |
| T02 | Instruksi dapat diproses oleh AI | Lulus |
| T03 | Hasil AI ditampilkan pada antarmuka | Lulus |
| T04 | Hasil AI tersimpan pada riwayat | Lulus |
| T05 | Riwayat tetap tersedia setelah aplikasi dijalankan ulang | Lulus |
| T06 | Pengujian otomatis | 25 tes lulus |
| T07 | Pemeriksaan format perubahan Git | Lulus |

## Kesimpulan
Fungsi dasar prototipe berhasil diuji pada lingkungan pengembangan.
Pengujian ini belum membuktikan kualitas jawaban AI, efektivitas
untuk pekerjaan guru, atau kelayakan penggunaan di sekolah.

## Pengujian lanjutan
1. Validasi kebutuhan guru SMP/MTs.
2. Evaluasi akurasi dan relevansi hasil AI.
3. Evaluasi kemudahan penggunaan.
4. Identifikasi risiko dan kesalahan keluaran AI.
5. Dokumentasi masukan dari calon pengguna.

Catatan: hasil pengujian fungsional di atas berdasarkan pemeriksaan
pengembang. Pengujian pengguna dan evaluasi kualitas belum dilakukan.
