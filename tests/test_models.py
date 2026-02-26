from task_manager.models.task import Task, TaskFactory

def test_task_factory_create_task():
    """Tests the TaskFactory.create_task method."""
    text = "Test Task"
    task = TaskFactory.create_task(text)
    assert isinstance(task, Task)
    assert task.text == text
    assert task.completed is False

def test_task_factory_create_completed_task():
    """Tests the TaskFactory.create_task method with completed=True."""
    text = "Completed Task"
    task = TaskFactory.create_task(text, completed=True)
    assert task.text == text
    assert task.completed is True
