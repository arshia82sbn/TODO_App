from unittest.mock import MagicMock

import pytest

from task_manager.core.task_service import TaskService
from task_manager.infra.repository import BaseRepository
from task_manager.models.task import Task


@pytest.fixture
def mock_repo():
    repo = MagicMock(spec=BaseRepository)
    repo.load_all.return_value = [Task(text="Initial Task")]
    return repo


def test_service_initialization(mock_repo):
    service = TaskService(repository=mock_repo)
    assert len(service.get_tasks()) == 1
    assert service.get_tasks()[0].text == "Initial Task"


def test_service_add_task(mock_repo):
    service = TaskService(repository=mock_repo)
    service.add_task("New Task")
    assert len(service.get_tasks()) == 2
    assert service.get_tasks()[1].text == "New Task"
    assert mock_repo.save_all.called


def test_service_toggle_task(mock_repo):
    service = TaskService(repository=mock_repo)
    service.toggle_task(0)
    assert service.get_tasks()[0].completed is True
    assert mock_repo.save_all.called


def test_service_delete_task(mock_repo):
    service = TaskService(repository=mock_repo)
    service.delete_task(0)
    assert len(service.get_tasks()) == 0
    assert mock_repo.save_all.called
