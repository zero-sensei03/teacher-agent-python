import pytest

from src.agent.validation import validate_instruction


def test_validate_instruction_trims_whitespace():
    assert validate_instruction("  Buat materi IPA  ") == "Buat materi IPA"


def test_validate_instruction_rejects_empty_text():
    with pytest.raises(ValueError, match="tidak boleh kosong"):
        validate_instruction("   ")


def test_validate_instruction_rejects_non_string():
    with pytest.raises(TypeError, match="harus berupa teks"):
        validate_instruction(None)


def test_validate_instruction_rejects_text_over_limit():
    with pytest.raises(ValueError, match="5000 karakter"):
        validate_instruction("a" * 5001)
