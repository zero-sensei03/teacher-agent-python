# Teacher Assistant Agent

Prototipe aplikasi berbasis Python dan Streamlit untuk mengeksplorasi penerapan AI Agent dalam membantu pekerjaan guru SMP/MTs.

## Status Proyek

Tahap pengembangan fondasi aplikasi.

Fitur utama belum ditetapkan karena rancangan prototipe perlu disesuaikan dengan hasil analisis kebutuhan penelitian.

## Teknologi

- Python 3.12
- Streamlit 1.66.1
- Git

## Persiapan

Pastikan Python 3.12 atau versi kompatibel telah terpasang.

### 1. Clone atau buka direktori proyek

Jika proyek sudah tersedia secara lokal, masuk ke direktori proyek.

### 2. Buat virtual environment

```bash
python3 -m venv .venv
```

### 3. Aktifkan virtual environment

Linux:

```bash
source .venv/bin/activate
```

### 4. Instal dependensi

```bash
python -m pip install -r requirements.txt
```

### 5. Jalankan aplikasi

```bash
streamlit run app.py
```

Buka alamat lokal yang ditampilkan oleh Streamlit di browser.

## Struktur Proyek

```text
teacher-assistant-agent/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   └── agent/
│       └── __init__.py
└── tests/
```

## Prinsip Pengembangan

- Fitur dikembangkan secara bertahap berdasarkan kebutuhan penelitian.
- Hasil AI harus dapat diperiksa oleh guru sebelum digunakan.
- Data pribadi guru dan siswa harus dilindungi.
- Hasil AI tidak dianggap selalu benar.
- Pengujian dilakukan sebelum fitur dinyatakan siap digunakan.
