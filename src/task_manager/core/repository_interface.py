from abc import ABC, abstractmethod

from task_manager.models.task import Task


# Strategy Pattern: Defines a common interface for different storage strategies.
class BaseRepository(ABC):
    """Abstract base class for task repositories."""

    @abstractmethod
    def load_all(self) -> list[Task]:
        """Loads all tasks from storage."""
        pass

    @abstractmethod
    def save_all(self, tasks: list[Task]) -> None:
        """Saves all tasks to storage."""
        pass
