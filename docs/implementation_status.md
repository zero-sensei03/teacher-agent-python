# Status Implementasi Prototipe

## Sudah dibuat
- Struktur awal proyek Python.
- Validasi instruksi.
- Daftar empat area pekerjaan guru.
- Struktur hasil workflow.
- Integrasi provider OpenAI dan Google Gemini.
- Konfigurasi provider melalui environment dan `.env`.
- Workflow dengan prompt khusus untuk setiap area pekerjaan.
- Antarmuka Streamlit.
- Penyimpanan riwayat menggunakan SQLite.
- Tampilan 20 riwayat terbaru.
- Pengujian otomatis untuk konfigurasi, provider, validasi,
  workflow, hasil, area pekerjaan, dan riwayat.

## Status pengujian terakhir
- 25 tes lulus.
- `git diff --check` bersih sebelum commit dokumentasi.

## Belum diselesaikan atau perlu diverifikasi
- Evaluasi kualitas hasil AI berdasarkan kebutuhan guru.
- Pengujian penggunaan oleh guru SMP/MTs.
- Evaluasi akurasi, relevansi, dan kemudahan penggunaan.
- Penanganan penghapusan riwayat.
- Kebijakan retensi dan perlindungan data riwayat.
- Pengujian integrasi API nyata untuk kedua provider.
- Dokumentasi hasil evaluasi dan keterbatasan prototipe.

## Catatan penelitian
Empat area pekerjaan saat ini merupakan kategori awal prototipe,
bukan hasil final analisis kebutuhan. Validasi melalui wawancara,
observasi, atau metode penelitian yang sesuai masih diperlukan.
