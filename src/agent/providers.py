"""Adapter untuk provider OpenAI dan Google Gemini."""

from google import genai
from openai import OpenAI

from src.agent.config import AISettings, get_ai_settings
from src.agent.validation import validate_instruction


def generate_text(
    prompt: str,
    settings: AISettings | None = None,
) -> str:
    """Menghasilkan teks menggunakan provider AI yang dikonfigurasi."""
    cleaned_prompt = validate_instruction(prompt)
    settings = settings or get_ai_settings()

    if settings.provider == "openai":
        client = OpenAI(api_key=settings.api_key)
        response = client.responses.create(
            model=settings.model,
            input=cleaned_prompt,
        )
        result = response.output_text

    elif settings.provider == "gemini":
        client = genai.Client(api_key=settings.api_key)
        response = client.models.generate_content(
            model=settings.model,
            contents=cleaned_prompt,
        )
        result = response.text

    else:
        raise ValueError(f"Provider tidak didukung: {settings.provider}")

    if not result or not result.strip():
        raise RuntimeError("Provider AI mengembalikan hasil kosong.")

    return result.strip()
