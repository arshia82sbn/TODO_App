from abc import ABC, abstractmethod

from task_manager.models.task import Task


class BaseRepository(ABC):
    """Abstract base class for task repositories.

    This interface defines the Strategy Pattern for task persistence.
    """

    @abstractmethod
    def load_all(self) -> list[Task]:
        """Loads all tasks from the storage backend."""
        pass

    @abstractmethod
    def save_all(self, tasks: list[Task]) -> None:
        """Saves all tasks to the storage backend."""
        pass
