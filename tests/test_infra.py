from pathlib import Path

from task_manager.infra.repository import JsonTaskRepository
from task_manager.models.task import Task, TaskFactory


def test_task_serialization() -> None:
    task = Task(text="Test Task", completed=True)
    data = task.to_dict()
    assert data == {"text": "Test Task", "completed": True}

    new_task = Task.from_dict(data)
    assert new_task.text == "Test Task"
    assert new_task.completed is True


def test_task_factory() -> None:
    task = TaskFactory.create_task("Factory Task", completed=True)
    assert isinstance(task, Task)
    assert task.text == "Factory Task"
    assert task.completed is True


def test_repository_load_save(tmp_path: Path) -> None:
    filepath = tmp_path / "tasks.json"
    repo = JsonTaskRepository(filepath=str(filepath))

    tasks = [Task(text="Task 1"), Task(text="Task 2", completed=True)]
    repo.save_all(tasks)

    loaded_tasks = repo.load_all()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].text == "Task 1"
    assert loaded_tasks[1].completed is True


def test_repository_corrupted_file(tmp_path: Path) -> None:
    filepath = tmp_path / "corrupted.json"
    filepath.write_text("invalid json")
    repo = JsonTaskRepository(filepath=str(filepath))
    assert repo.load_all() == []
