from task_manager.models.task import Task


def test_task_creation():
    """Tests the creation of a Task instance."""
    task = Task(text="Test Task")
    assert task.text == "Test Task"
    assert task.completed is False

def test_task_toggle():
    """Tests that a task can be manually toggled (although service does it)."""
    task = Task(text="Test Task")
    task.completed = True
    assert task.completed is True

def test_task_to_dict():
    """Tests the to_dict method."""
    task = Task(text="Test Task", completed=True)
    expected = {"text": "Test Task", "completed": True}
    assert task.to_dict() == expected

def test_task_from_dict():
    """Tests the from_dict class method."""
    data = {"text": "From Dict", "completed": True}
    task = Task.from_dict(data)
    assert task.text == "From Dict"
    assert task.completed is True

def test_task_from_dict_defaults():
    """Tests the from_dict class method with missing fields."""
    task = Task.from_dict({})
    assert task.text == ""
    assert task.completed is False
