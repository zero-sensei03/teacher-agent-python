"""Daftar sementara area pekerjaan guru."""


TASK_AREAS = [
    "Penyusunan materi pembelajaran",
    "Pembuatan soal dan pembahasan",
    "Pemeriksaan jawaban dan pengolahan nilai",
    "Administrasi pembelajaran",
]


def get_task_areas() -> list[str]:
    """Mengembalikan daftar area pekerjaan guru."""
    return TASK_AREAS.copy()
