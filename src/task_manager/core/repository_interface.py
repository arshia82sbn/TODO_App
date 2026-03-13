from abc import ABC, abstractmethod

from task_manager.models.task import Task


class BaseRepository(ABC):
    """Abstract base class for task repositories.

    This interface defines the required methods for any repository
    implementation, allowing the core logic to remain decoupled from
    specific storage mechanisms (Strategy Pattern).
    """

    @abstractmethod
    def load_all(self) -> list[Task]:
        """Loads all tasks from storage.

        Returns:
            List[Task]: A list of Task objects.
        """
        pass

    @abstractmethod
    def save_all(self, tasks: list[Task]) -> None:
        """Saves all tasks to storage.

        Args:
            tasks (List[Task]): The list of Task objects to save.
        """
        pass
