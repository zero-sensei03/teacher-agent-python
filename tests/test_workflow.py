import pytest

from src.agent.workflow import run_workflow


def test_run_workflow_accepts_valid_instruction():
    result = run_workflow("Buat materi pembelajaran IPA")

    assert result.success is True
    assert result.content == ""
    assert "berhasil divalidasi" in result.message
    assert result.requires_review is True


def test_run_workflow_rejects_empty_instruction():
    result = run_workflow("   ")

    assert result.success is False
    assert result.content == ""
    assert "tidak boleh kosong" in result.message


def test_run_workflow_rejects_non_string_instruction():
    result = run_workflow(None)

    assert result.success is False
    assert result.content == ""
    assert "harus berupa teks" in result.message


def test_run_workflow_rejects_instruction_over_limit():
    result = run_workflow("a" * 5001)

    assert result.success is False
    assert result.content == ""
    assert "5000 karakter" in result.message

