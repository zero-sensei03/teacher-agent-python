from src.agent import workflow


def test_run_workflow_generates_content(monkeypatch):
    calls = {}

    def fake_generate_text(prompt):
        calls["prompt"] = prompt
        return "Materi IPA tentang ekosistem."

    monkeypatch.setattr(workflow, "generate_text", fake_generate_text)

    result = workflow.run_workflow(
        "Buat materi tentang ekosistem",
        "Penyusunan materi pembelajaran",
    )

    assert result.success is True
    assert result.content == "Materi IPA tentang ekosistem."
    assert result.requires_review is True
    assert "ekosistem" in calls["prompt"]
    assert "Penyusunan materi pembelajaran" in calls["prompt"]


def test_run_workflow_rejects_empty_instruction():
    result = workflow.run_workflow("   ")

    assert result.success is False
    assert result.content == ""
    assert "tidak boleh kosong" in result.message


def test_run_workflow_rejects_non_string_instruction():
    result = workflow.run_workflow(None)

    assert result.success is False
    assert "harus berupa teks" in result.message


def test_run_workflow_rejects_instruction_over_limit():
    result = workflow.run_workflow("a" * 5001)

    assert result.success is False
    assert "5000 karakter" in result.message


def test_run_workflow_handles_provider_error(monkeypatch):
    def fake_generate_text(prompt):
        raise RuntimeError("Simulated provider failure")

    monkeypatch.setattr(workflow, "generate_text", fake_generate_text)

    result = workflow.run_workflow("Buat materi IPA")

    assert result.success is False
    assert result.content == ""
    assert "Gagal menghubungi provider AI" in result.message
    assert "Simulated provider failure" not in result.message
