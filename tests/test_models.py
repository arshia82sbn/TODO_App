from task_manager.models.task import Task, TaskFactory


def test_task_creation():
    task = Task(text="Test Task")
    assert task.text == "Test Task"
    assert task.completed is False


def test_task_to_dict():
    task = Task(text="Test Task", completed=True)
    expected = {"text": "Test Task", "completed": True}
    assert task.to_dict() == expected


def test_task_from_dict():
    data = {"text": "Test Task", "completed": True}
    task = Task.from_dict(data)
    assert task.text == "Test Task"
    assert task.completed is True


def test_task_factory_create_task():
    task = TaskFactory.create_task("Factory Task")
    assert isinstance(task, Task)
    assert task.text == "Factory Task"
    assert task.completed is False


def test_task_factory_create_task_completed():
    task = TaskFactory.create_task("Completed Task", completed=True)
    assert task.text == "Completed Task"
    assert task.completed is True
