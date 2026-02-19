from task_manager.models.task import Task, TaskFactory


def test_task_creation():
    """Tests basic Task creation and defaults."""
    task = Task(text="Buy milk")
    assert task.text == "Buy milk"
    assert task.completed is False


def test_task_to_dict():
    """Tests Task serialization to dictionary."""
    task = Task(text="Buy milk", completed=True)
    expected = {"text": "Buy milk", "completed": True}
    assert task.to_dict() == expected


def test_task_from_dict():
    """Tests Task deserialization from dictionary."""
    data = {"text": "Buy milk", "completed": True}
    task = Task.from_dict(data)
    assert task.text == "Buy milk"
    assert task.completed is True


def test_task_factory_create():
    """Tests Task creation via TaskFactory."""
    task = TaskFactory.create_task(text="Clean room", completed=True)
    assert isinstance(task, Task)
    assert task.text == "Clean room"
    assert task.completed is True


def test_task_factory_defaults():
    """Tests TaskFactory defaults."""
    task = TaskFactory.create_task(text="Exercise")
    assert task.completed is False
