from task_manager.models.task import Task, TaskFactory


def test_create_task():
    """Tests that TaskFactory correctly creates a Task instance."""
    task = TaskFactory.create_task("Test Task")
    assert isinstance(task, Task)
    assert task.text == "Test Task"
    assert task.completed is False


def test_create_completed_task():
    """Tests that TaskFactory correctly creates a completed Task instance."""
    task = TaskFactory.create_task("Completed Task", completed=True)
    assert isinstance(task, Task)
    assert task.text == "Completed Task"
    assert task.completed is True
