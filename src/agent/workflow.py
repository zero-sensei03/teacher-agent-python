"""Workflow untuk menghasilkan konten dengan bantuan AI."""

from src.agent.providers import generate_text
from src.agent.result import AgentResult
from src.agent.validation import validate_instruction


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

    prompt = f"""
Anda adalah Teacher Assistant Agent untuk membantu guru SMP/MTs.

Area pekerjaan: {task_area}

Instruksi guru:
{cleaned_instruction}

Ketentuan:
- Gunakan bahasa Indonesia yang jelas dan sesuai kebutuhan guru.
- Susun hasil secara terstruktur dan praktis.
- Jangan mengarang fakta atau referensi.
- Jika informasi penting kurang, nyatakan asumsi yang digunakan.
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
        # else:
        #     message = f"Kesalahan provider AI: {type(exc).__name__}"

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
