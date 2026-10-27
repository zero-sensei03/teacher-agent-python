"""Penyimpanan riwayat hasil AI menggunakan SQLite."""

import sqlite3
from pathlib import Path

DB_PATH = Path("data/history.db")


def init_history_db() -> None:
    """Membuat database dan tabel riwayat jika belum tersedia."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_area TEXT NOT NULL,
                instruction TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def save_history(
    task_area: str,
    instruction: str,
    content: str,
) -> int:
    """Menyimpan hasil AI dan mengembalikan ID riwayat."""
    init_history_db()

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            """
            INSERT INTO history (task_area, instruction, content)
            VALUES (?, ?, ?)
            """,
            (task_area, instruction, content),
        )
        return cursor.lastrowid


def get_history(limit: int = 50) -> list[dict]:
    """Mengambil riwayat terbaru terlebih dahulu."""
    if limit < 1:
        raise ValueError("Limit harus lebih besar dari nol.")

    init_history_db()

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT id, task_area, instruction, content, created_at
            FROM history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return [dict(row) for row in rows]
