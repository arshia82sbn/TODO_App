import json
import os

from task_manager.core.repository_interface import BaseRepository
from task_manager.models.task import Task


class TaskRepository(BaseRepository):
    """Handles persistence of tasks to a JSON file.

    This class implements the Repository Pattern to abstract the data storage
    mechanism from the rest of the application.
    """

    def __init__(self, filepath: str = "tasks.json") -> None:
        """Initializes the repository with a specific file path.

        Args:
            filepath (str): Path to the JSON file where tasks are stored.
        """
        self.filepath = filepath

    def load_all(self) -> list[Task]:
        """Loads all tasks from the JSON file.

        Returns:
            List[Task]: A list of Task objects.
        """
        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath) as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (OSError, json.JSONDecodeError):
            # Fallback to empty list if file is corrupted or unreadable
            return []

    def save_all(self, tasks: list[Task]) -> None:
        """Saves all tasks to the JSON file.

        Args:
            tasks (List[Task]): The list of Task objects to save.
        """
        data = [task.to_dict() for task in tasks]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)
