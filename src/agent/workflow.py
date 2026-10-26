"""Workflow dasar untuk memproses instruksi guru."""

from src.agent.result import AgentResult
from src.agent.validation import validate_instruction


def run_workflow(instruction: str) -> AgentResult:
    """Memvalidasi instruksi dan mengembalikan status workflow."""

    try:
        validate_instruction(instruction)
    except (TypeError, ValueError) as exc:
        return AgentResult(
            success=False,
            content="",
            message=str(exc),
        )

    return AgentResult(
        success=True,
        content="",
        message=(
            "Instruksi berhasil divalidasi. "
            "Pemrosesan AI belum diimplementasikan."
        ),
    )
