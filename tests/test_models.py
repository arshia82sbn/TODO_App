from task_manager.models.task import Task, TaskFactory


def test_task_factory_create_task() -> None:
    """Tests the TaskFactory.create_task method."""
    task = TaskFactory.create_task("Test Task")
    assert isinstance(task, Task)
    assert task.text == "Test Task"
    assert task.completed is False


def test_task_factory_create_completed_task() -> None:
    """Tests creating a completed task via TaskFactory."""
    task = TaskFactory.create_task("Completed Task", completed=True)
    assert task.text == "Completed Task"
    assert task.completed is True
