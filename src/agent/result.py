"""Struktur hasil kerja agent."""

from dataclasses import dataclass


@dataclass
class AgentResult:
    """Mewakili hasil kerja agent yang dapat diperiksa pengguna."""

    success: bool
    content: str
    message: str
    requires_review: bool = True
