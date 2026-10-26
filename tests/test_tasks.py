from src.agent.tasks import get_task_areas


def test_get_task_areas_returns_expected_items():
    areas = get_task_areas()

    assert len(areas) == 4
    assert "Penyusunan materi pembelajaran" in areas
    assert "Pembuatan soal dan pembahasan" in areas


def test_get_task_areas_returns_independent_list():
    areas = get_task_areas()
    areas.clear()

    assert len(get_task_areas()) == 4
