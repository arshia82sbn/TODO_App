from task_manager.models.task import Task, TaskFactory


def test_task_factory_create_task():
    """Tests that the TaskFactory correctly creates a Task instance."""
    text = "Test Task"
    task = TaskFactory.create_task(text)

    assert isinstance(task, Task)
    assert task.text == text
    assert task.completed is False
