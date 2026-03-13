from task_manager.api.gui import TaskApp
from task_manager.core.task_service import TaskService
from task_manager.infra.repository import TaskRepository


def main() -> None:
    """Entry point for the task manager application.

    Initializes the infrastructure, core service, and UI with
    dependency injection.
    """
    repository = TaskRepository()
    service = TaskService(repository=repository)
    app = TaskApp(service=service)
    app.run()

if __name__ == "__main__":
    main()
