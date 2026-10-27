from types import SimpleNamespace

import pytest

from src.agent.config import AISettings
from src.agent import providers


def test_generate_text_with_openai(monkeypatch):
    calls = {}

    class FakeOpenAI:
        def __init__(self, api_key):
            calls["api_key"] = api_key
            self.responses = self

        def create(self, **kwargs):
            calls["request"] = kwargs
            return SimpleNamespace(output_text="  Hasil OpenAI  ")

    monkeypatch.setattr(providers, "OpenAI", FakeOpenAI)

    settings = AISettings("openai", "fake-key", "fake-model")
    result = providers.generate_text("  Buat materi IPA  ", settings)

    assert result == "Hasil OpenAI"
    assert calls["api_key"] == "fake-key"
    assert calls["request"]["model"] == "fake-model"
    assert calls["request"]["input"] == "Buat materi IPA"


def test_generate_text_with_gemini(monkeypatch):
    calls = {}

    class FakeGemini:
        def __init__(self, api_key):
            calls["api_key"] = api_key
            self.models = self

        def generate_content(self, **kwargs):
            calls["request"] = kwargs
            return SimpleNamespace(text="Hasil Gemini")

    monkeypatch.setattr(providers.genai, "Client", FakeGemini)

    settings = AISettings("gemini", "fake-key", "fake-model")
    result = providers.generate_text("Buat materi IPA", settings)

    assert result == "Hasil Gemini"
    assert calls["api_key"] == "fake-key"
    assert calls["request"]["model"] == "fake-model"
    assert calls["request"]["contents"] == "Buat materi IPA"


def test_generate_text_rejects_empty_prompt():
    settings = AISettings("openai", "fake-key", "fake-model")

    with pytest.raises(ValueError, match="tidak boleh kosong"):
        providers.generate_text("   ", settings)


def test_generate_text_rejects_empty_response(monkeypatch):
    class FakeOpenAI:
        def __init__(self, api_key):
            self.responses = self

        def create(self, **kwargs):
            return SimpleNamespace(output_text="  ")

    monkeypatch.setattr(providers, "OpenAI", FakeOpenAI)

    settings = AISettings("openai", "fake-key", "fake-model")

    with pytest.raises(RuntimeError, match="hasil kosong"):
        providers.generate_text("Buat materi IPA", settings)
