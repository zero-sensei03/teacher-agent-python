# Teacher Assistant Agent

Prototipe asisten AI untuk membantu pekerjaan guru SMP/MTs.

## Fitur
- Empat area pekerjaan guru.
- Integrasi provider OpenAI dan Google Gemini.
- Validasi instruksi maksimal 5.000 karakter.
- Prompt khusus berdasarkan area pekerjaan.
- Riwayat hasil AI menggunakan SQLite.
- Peninjauan hasil oleh guru sebelum digunakan.

## Persiapan
Aktifkan virtual environment:

    source .venv/bin/activate

Instal dependensi:

    pip install -r requirements.txt

Konfigurasikan provider dan API key melalui file `.env`.
Gunakan `.env.example` sebagai acuan. Jangan commit API key.

## Menjalankan aplikasi

    streamlit run app.py

## Menjalankan pengujian

    python -m pytest -q

## Struktur utama
- `app.py`: antarmuka Streamlit.
- `src/agent/config.py`: konfigurasi provider AI.
- `src/agent/providers.py`: integrasi API AI.
- `src/agent/tasks.py`: daftar area pekerjaan guru.
- `src/agent/validation.py`: validasi instruksi.
- `src/agent/workflow.py`: alur pemrosesan instruksi.
- `src/agent/result.py`: struktur hasil workflow.
- `src/agent/history.py`: penyimpanan dan pembacaan riwayat.
- `tests/`: pengujian otomatis.
- `data/history.db`: database riwayat yang dibuat otomatis.

## Catatan
Prototipe masih memerlukan evaluasi dengan kebutuhan guru yang nyata.
Hasil AI harus diperiksa sebelum digunakan. Hindari memasukkan data
pribadi atau sensitif siswa.
