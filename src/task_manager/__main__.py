from task_manager.api import TaskApp


def main() -> None:
    """Entry point for the task manager application."""
    app = TaskApp()
    app.run()


if __name__ == "__main__":
    main()
