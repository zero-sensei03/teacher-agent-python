"""Validasi input dasar untuk alur kerja agent."""


def validate_instruction(instruction: str) -> str:
    """Memvalidasi instruksi dan mengembalikan teks yang sudah dirapikan."""

    if not isinstance(instruction, str):
        raise TypeError("Instruksi harus berupa teks.")

    cleaned_instruction = instruction.strip()

    if not cleaned_instruction:
        raise ValueError("Instruksi tidak boleh kosong.")

    if len(cleaned_instruction) > 5000:
        raise ValueError("Instruksi tidak boleh melebihi 5000 karakter.")

    return cleaned_instruction
