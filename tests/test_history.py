import pytest

from src.agent import history


@pytest.fixture
def temporary_db(tmp_path, monkeypatch):
    """Gunakan database sementara agar tidak mengubah database asli."""
    monkeypatch.setattr(history, "DB_PATH", tmp_path / "history.db")
    history.init_history_db()


def test_save_and_get_history(temporary_db):
    history.save_history(
        "Penyusunan materi pembelajaran",
        "Buat materi IPA kelas VII",
        "Materi tentang ekosistem",
    )

    results = history.get_history()

    assert len(results) == 1
    assert results[0]["task_area"] == "Penyusunan materi pembelajaran"
    assert results[0]["instruction"] == "Buat materi IPA kelas VII"
    assert results[0]["content"] == "Materi tentang ekosistem"


def test_history_is_ordered_newest_first(temporary_db):
    history.save_history("Area 1", "Instruksi 1", "Hasil 1")
    history.save_history("Area 2", "Instruksi 2", "Hasil 2")

    results = history.get_history()

    assert len(results) == 2
    assert results[0]["content"] == "Hasil 2"
    assert results[1]["content"] == "Hasil 1"


def test_get_history_respects_limit(temporary_db):
    history.save_history("Area 1", "Instruksi 1", "Hasil 1")
    history.save_history("Area 2", "Instruksi 2", "Hasil 2")

    results = history.get_history(limit=1)

    assert len(results) == 1
    assert results[0]["content"] == "Hasil 2"


def test_get_history_rejects_invalid_limit(temporary_db):
    with pytest.raises(ValueError, match="lebih besar dari nol"):
        history.get_history(limit=0)
