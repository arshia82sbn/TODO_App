from task_manager.models.task import Task, TaskFactory


def test_task_factory_create_task():
    task = TaskFactory.create_task("Test Task")
    assert isinstance(task, Task)
    assert task.text == "Test Task"
    assert task.completed is False

    task_completed = TaskFactory.create_task("Done Task", completed=True)
    assert task_completed.text == "Done Task"
    assert task_completed.completed is True


def test_task_factory_from_dict():
    data = {"text": "From Dict", "completed": True}
    task = TaskFactory.from_dict(data)
    assert task is not None
    assert task.text == "From Dict"
    assert task.completed is True


def test_task_factory_from_dict_invalid():
    data = {"not_text": "Something"}
    task = TaskFactory.from_dict(data)
    assert task is None
