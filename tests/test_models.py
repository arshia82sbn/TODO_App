from task_manager.models.task import Task, TaskFactory


def test_task_factory_create_task():
    """Confirms TaskFactory.create_task returns a Task instance with the expected attributes."""
    text = "Test Task"
    completed = True
    task = TaskFactory.create_task(text, completed)

    assert isinstance(task, Task)
    assert task.text == text
    assert task.completed == completed


def test_task_factory_create_default_task():
    """Confirms TaskFactory.create_task handles default values correctly."""
    text = "Default Task"
    task = TaskFactory.create_task(text)

    assert task.text == text
    assert task.completed is False
