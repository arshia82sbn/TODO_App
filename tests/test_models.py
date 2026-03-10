from task_manager.models.task import Task, TaskFactory


def test_task_factory_create_task() -> None:
    """Test that TaskFactory correctly creates a Task instance."""
    task = TaskFactory.create_task("Test Task")
    assert isinstance(task, Task)
    assert task.text == "Test Task"
    assert task.completed is False


def test_task_factory_create_completed_task() -> None:
    """Test that TaskFactory correctly creates a completed Task instance."""
    task = TaskFactory.create_task("Completed Task", completed=True)
    assert task.text == "Completed Task"
    assert task.completed is True
