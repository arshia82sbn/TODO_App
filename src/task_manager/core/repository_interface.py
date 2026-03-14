from abc import ABC, abstractmethod

from task_manager.models.task import Task


class BaseRepository(ABC):
    """Abstract base class for task repositories.

    This interface implements the Strategy Pattern, allowing different persistence
    mechanisms to be used interchangeably.
    """

    @abstractmethod
    def load_all(self) -> list[Task]:
        """Loads all tasks from the storage.

        Returns:
            List[Task]: A list of Task objects.
        """
        pass

    @abstractmethod
    def save_all(self, tasks: list[Task]) -> None:
        """Saves all tasks to the storage.

        Args:
            tasks (List[Task]): The list of Task objects to save.
        """
        pass
