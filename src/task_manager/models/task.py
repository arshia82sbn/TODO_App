from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Task:
    """Represents a daily task.

    Attributes:
        text (str): The description of the task.
        completed (bool): Whether the task is completed.
    """
    text: str
    completed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Converts the task to a dictionary for JSON serialization.

        Returns:
            Dict[str, Any]: Dictionary representation of the task.
        """
        return {
            "text": self.text,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Creates a Task instance from a dictionary.

        Args:
            data (Dict[str, Any]): Dictionary containing task data.

        Returns:
            Task: A new Task instance.
        """
        return cls(
            text=data.get("text", ""),
            completed=data.get("completed", False)
        )


class TaskFactory:
    """Factory for creating Task instances.

    This class implements the Factory pattern to centralize task creation.
    """

    @staticmethod
    def create_task(text: str, completed: bool = False) -> Task:
        """Creates a new Task instance.

        Args:
            text (str): The description of the task.
            completed (bool): Whether the task is completed. Defaults to False.

        Returns:
            Task: A new Task instance.
        """
        return Task(text=text, completed=completed)
