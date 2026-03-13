from task_manager.core.repository_interface import BaseRepository
from task_manager.models.task import Task


class TaskService:
    """Business logic for managing tasks.

    This class acts as a Service/Facade, providing a clean API for the GUI
    to interact with tasks while hiding the details of storage. It depends
    on the BaseRepository interface (Dependency Inversion Principle).
    """

    def __init__(self, repository: BaseRepository) -> None:
        """Initializes the service with a repository.

        Args:
            repository (BaseRepository): The concrete repository implementation.
        """
        self.repository = repository
        self.tasks: list[Task] = self.repository.load_all()

    def get_tasks(self) -> list[Task]:
        """Returns the current list of tasks.

        Returns:
            list[Task]: All tasks.
        """
        return self.tasks

    def add_task(self, text: str) -> Task:
        """Adds a new task.

        Args:
            text (str): The task description.

        Returns:
            Task: The newly created task.
        """
        new_task = Task(text=text)
        self.tasks.append(new_task)
        self.repository.save_all(self.tasks)
        return new_task

    def toggle_task(self, index: int) -> None:
        """Toggles the completion status of a task.

        Args:
            index (int): The index of the task in the list.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self.repository.save_all(self.tasks)

    def delete_task(self, index: int) -> None:
        """Deletes a task from the list.

        Args:
            index (int): The index of the task to delete.
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.repository.save_all(self.tasks)

    def refresh_tasks(self) -> None:
        """Reloads tasks from the repository."""
        self.tasks = self.repository.load_all()
