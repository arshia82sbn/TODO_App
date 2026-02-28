from typing import List, Optional

from task_manager.infra.repository import BaseRepository, TaskRepository
from task_manager.models.task import Task, TaskFactory


class TaskService:
    """Business logic for managing tasks.

    This class implements the Facade pattern to provide a clean API for the GUI
    while abstracting business logic and storage details.
    """

    def __init__(self, repository: Optional[BaseRepository] = None):
        """Initializes the service with a repository.

        Args:
            repository (Optional[BaseRepository]): The repository to use.
                Defaults to a new TaskRepository instance.
        """
        # Dependency Inversion: Depending on BaseRepository abstraction instead of TaskRepository.
        self.repository = repository or TaskRepository()
        self.tasks: List[Task] = self.repository.load_all()

    def get_tasks(self) -> List[Task]:
        """Returns the current list of tasks.

        Returns:
            List[Task]: All tasks.
        """
        return self.tasks

    def add_task(self, text: str) -> Task:
        """Adds a new task.

        Args:
            text (str): The task description.

        Returns:
            Task: The newly created task.
        """
        # Factory Pattern: Centralizing task creation using TaskFactory.
        new_task = TaskFactory.create_task(text=text)
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
