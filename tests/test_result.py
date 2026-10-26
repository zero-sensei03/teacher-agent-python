from src.agent.result import AgentResult


def test_agent_result_has_expected_values():
    result = AgentResult(
        success=True,
        content="Materi pembelajaran IPA",
        message="Hasil berhasil dibuat",
    )

    assert result.success is True
    assert result.content == "Materi pembelajaran IPA"
    assert result.message == "Hasil berhasil dibuat"
    assert result.requires_review is True


def test_agent_result_can_represent_failure():
    result = AgentResult(
        success=False,
        content="",
        message="Instruksi tidak valid",
    )

    assert result.success is False
    assert result.content == ""
