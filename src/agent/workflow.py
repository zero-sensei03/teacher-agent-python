"""Workflow untuk menghasilkan konten dengan bantuan AI."""

from src.agent.providers import generate_text
from src.agent.result import AgentResult
from src.agent.validation import validate_instruction


TASK_PROMPTS = {
    "Penyusunan materi pembelajaran": """
Susun materi dengan bagian:
1. Judul dan sasaran kelas
2. Tujuan pembelajaran
3. Penjelasan materi
4. Contoh yang relevan
5. Rangkuman
6. Pertanyaan evaluasi beserta kunci jawaban.
""",
    "Pembuatan soal dan pembahasan": """
Susun soal sesuai instruksi dengan bagian:
1. Mata pelajaran dan sasaran kelas
2. Tujuan atau kompetensi yang diukur
3. Soal
4. Kunci jawaban
5. Pembahasan setiap soal.
Pastikan soal jelas, tidak ambigu, dan sesuai tingkat kelas.
""",
    "Pemeriksaan jawaban dan pengolahan nilai": """
Bantu meninjau jawaban berdasarkan kriteria yang diberikan.
Sajikan rubrik penilaian, analisis jawaban, rekomendasi skor beserta
alasannya, dan catatan untuk guru.
Jangan mengarang jawaban siswa atau kriteria yang tidak diberikan.
Rekomendasi skor harus diverifikasi guru.
""",
    "Administrasi pembelajaran": """
Susun dokumen administrasi pembelajaran secara terstruktur,
konsisten, dan mudah disunting.
Jangan mengarang data sekolah, guru, atau peserta didik.
Nyatakan asumsi jika informasi penting belum diberikan.
""",
}


def run_workflow(
    instruction: str,
    task_area: str = "Pekerjaan guru",
) -> AgentResult:
    """Validasi instruksi, panggil AI, dan kembalikan hasilnya."""

    try:
        cleaned_instruction = validate_instruction(instruction)
    except (TypeError, ValueError) as exc:
        return AgentResult(
            success=False,
            content="",
            message=str(exc),
        )

    task_guidance = TASK_PROMPTS.get(
        task_area,
        "Berikan hasil yang terstruktur dan praktis sesuai instruksi guru.",
    )

    prompt = f"""
Anda adalah Teacher Assistant Agent untuk membantu guru SMP/MTs.

Area pekerjaan: {task_area}

Panduan area pekerjaan:
{task_guidance}

Instruksi guru:
{cleaned_instruction}

Ketentuan umum:
- Gunakan bahasa Indonesia yang jelas.
- Jangan mengarang fakta atau referensi.
- Nyatakan asumsi jika informasi penting kurang.
- Hasil wajib ditinjau guru sebelum digunakan.
""".strip()

    try:
        content = generate_text(prompt)

    except ValueError as exc:
        return AgentResult(
            success=False,
            content="",
            message=str(exc),
        )

    except Exception as exc:
        # Penanganan spesifik OpenAI hanya jika exception berasal dari SDK OpenAI.
        from openai import (
            APIConnectionError,
            AuthenticationError,
            BadRequestError,
            PermissionDeniedError,
            RateLimitError,
        )

        if isinstance(exc, AuthenticationError):
            message = "Autentikasi OpenAI gagal. Periksa API key."
        elif isinstance(exc, PermissionDeniedError):
            message = "Akses OpenAI ditolak. Periksa izin API key dan project."
        elif isinstance(exc, RateLimitError):
            code = getattr(exc, "code", None) or "unknown"
            error_type = getattr(exc, "type", None) or "unknown"
            status = getattr(exc, "status_code", None) or "unknown"
            message = (
                f"OpenAI API error: HTTP {status}; "
                f"code={code}; type={error_type}."
            )
        elif isinstance(exc, BadRequestError):
            message = (
                "Permintaan OpenAI tidak valid. Periksa nama model "
                "dan parameter permintaan."
            )
        elif isinstance(exc, APIConnectionError):
            message = "Tidak dapat terhubung ke OpenAI. Periksa koneksi internet."
        else:
            message = (
                "Gagal menghubungi provider AI. "
                "Periksa konfigurasi, koneksi internet, dan log aplikasi."
            )

        return AgentResult(
            success=False,
            content="",
            message=message,
        )

    return AgentResult(
        success=True,
        content=content,
        message="Hasil AI berhasil dibuat.",
        requires_review=True,
    )