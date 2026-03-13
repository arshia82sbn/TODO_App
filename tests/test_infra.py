from typing import Any

from task_manager.infra.repository import TaskRepository
from task_manager.models.task import Task


def test_task_serialization() -> None:
    task = Task(text="Test Task", completed=True)
    data = task.to_dict()
    assert data == {"text": "Test Task", "completed": True}

    new_task = Task.from_dict(data)
    assert new_task.text == "Test Task"
    assert new_task.completed is True


def test_repository_load_save(tmp_path: Any) -> None:
    expected_count = 2
    filepath = tmp_path / "tasks.json"
    repo = TaskRepository(filepath=str(filepath))

    tasks = [Task(text="Task 1"), Task(text="Task 2", completed=True)]
    repo.save_all(tasks)

    loaded_tasks = repo.load_all()
    assert len(loaded_tasks) == expected_count
    assert loaded_tasks[0].text == "Task 1"
    assert loaded_tasks[1].completed is True


def test_repository_corrupted_file(tmp_path: Any) -> None:
    filepath = tmp_path / "corrupted.json"
    filepath.write_text("invalid json")
    repo = TaskRepository(filepath=str(filepath))
    assert repo.load_all() == []
