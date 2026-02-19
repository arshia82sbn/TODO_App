from unittest.mock import MagicMock

import pytest

from task_manager.core.task_service import TaskService
from task_manager.models.task import Task


@pytest.fixture
def mock_repo():
    """Fixture for a mocked repository."""
    repo = MagicMock()
    repo.load_all.return_value = [Task(text="Initial Task")]
    return repo


def test_service_initialization(mock_repo):
    """Tests that the service initializes with tasks from the repository."""
    service = TaskService(repository=mock_repo)
    assert len(service.get_tasks()) == 1
    assert service.get_tasks()[0].text == "Initial Task"


def test_service_add_task(mock_repo):
    """Tests adding a new task through the service."""
    service = TaskService(repository=mock_repo)
    service.add_task("New Task")
    assert len(service.get_tasks()) == 2
    assert service.get_tasks()[1].text == "New Task"
    assert mock_repo.save_all.called


def test_service_toggle_task(mock_repo):
    """Tests toggling a task's completion status."""
    service = TaskService(repository=mock_repo)
    service.toggle_task(0)
    assert service.get_tasks()[0].completed is True
    assert mock_repo.save_all.called

    service.toggle_task(0)
    assert service.get_tasks()[0].completed is False


def test_service_toggle_task_invalid_index(mock_repo):
    """Tests toggling a task with an out-of-bounds index."""
    service = TaskService(repository=mock_repo)
    service.toggle_task(100)  # Should not raise error
    assert mock_repo.save_all.call_count == 0


def test_service_delete_task(mock_repo):
    """Tests deleting a task."""
    service = TaskService(repository=mock_repo)
    service.delete_task(0)
    assert len(service.get_tasks()) == 0
    assert mock_repo.save_all.called


def test_service_delete_task_invalid_index(mock_repo):
    """Tests deleting a task with an out-of-bounds index."""
    service = TaskService(repository=mock_repo)
    service.delete_task(100)  # Should not raise error
    assert mock_repo.save_all.call_count == 0


def test_service_refresh_tasks(mock_repo):
    """Tests refreshing tasks from the repository."""
    service = TaskService(repository=mock_repo)
    mock_repo.load_all.return_value = [Task(text="Refreshed Task")]
    service.refresh_tasks()
    assert len(service.get_tasks()) == 1
    assert service.get_tasks()[0].text == "Refreshed Task"
