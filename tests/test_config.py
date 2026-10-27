import pytest

from src.agent.config import get_ai_settings


def test_get_openai_settings(monkeypatch):
    monkeypatch.setenv("AI_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-test")

    settings = get_ai_settings()

    assert settings.provider == "openai"
    assert settings.api_key == "test-openai-key"
    assert settings.model == "gpt-test"


def test_get_gemini_settings(monkeypatch):
    monkeypatch.setenv("AI_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    monkeypatch.setenv("GEMINI_MODEL", "gemini-test")

    settings = get_ai_settings()

    assert settings.provider == "gemini"
    assert settings.api_key == "test-gemini-key"
    assert settings.model == "gemini-test"


def test_rejects_unknown_provider(monkeypatch):
    monkeypatch.setenv("AI_PROVIDER", "unknown")

    with pytest.raises(ValueError, match="AI_PROVIDER"):
        get_ai_settings()


def test_rejects_missing_api_key(monkeypatch):
    monkeypatch.setenv("AI_PROVIDER", "openai")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        get_ai_settings()
