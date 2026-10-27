"""Konfigurasi provider AI dari environment atau file .env."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AISettings:
    provider: str
    api_key: str
    model: str


def get_ai_settings() -> AISettings:
    """Ambil konfigurasi provider AI yang aktif."""
    provider = os.getenv("AI_PROVIDER", "openai").strip().lower()

    if provider == "openai":
        key_name = "OPENAI_API_KEY"
        model_name = "OPENAI_MODEL"
        default_model = "gpt-5.4-mini"
    elif provider == "gemini":
        key_name = "GEMINI_API_KEY"
        model_name = "GEMINI_MODEL"
        default_model = "gemini-3.8-flash"
    else:
        raise ValueError(
            "AI_PROVIDER harus bernilai 'openai' atau 'gemini'."
        )

    api_key = os.getenv(key_name, "").strip()
    if not api_key:
        raise ValueError(
            f"{key_name} belum diatur. Periksa file .env."
        )

    model = os.getenv(model_name, default_model).strip()
    if not model:
        raise ValueError(f"{model_name} tidak boleh kosong.")

    return AISettings(
        provider=provider,
        api_key=api_key,
        model=model,
    )
