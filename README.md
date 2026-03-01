# ✅ Daily Task Manager

A professional, refactored task manager built with **CustomTkinter**.

![Todo App](demo.gif)

## 🚀 Features

- ➕ **Add Tasks**: Easily enter new tasks.
- ✅ **Toggle Tasks**: Mark tasks as completed with a visual strike-through.
- ❌ **Delete Tasks**: Remove tasks instantly.
- 💾 **Persistence**: Automatic saving to `tasks.json`.
- 🏗️ **Clean Architecture**: Implemented with Strategy, Factory, Repository and Facade patterns.
- 🧪 **Tested**: Unit tests included.

## 🏗️ Design Patterns

This project leverages several design patterns to ensure maintainability and scalability:
- **Factory Pattern**: Centralized task creation through `TaskFactory`.
- **Strategy Pattern**: Abstract persistence interface with `BaseRepository`.
- **Repository Pattern**: JSON-based task storage implementation.
- **Facade Pattern**: Clean API for GUI interactions via `TaskService`.

## 📦 Installation

```bash
pip install .
```

Or for development:

```bash
pip install -e .
```

## 🛠️ Usage

Run the application:

```bash
python -m task_manager
```

Or if installed as a package:

```bash
task-manager
```

## 🏗️ Project Structure

- `src/task_manager/api/`: GUI implementation (Public API).
- `src/task_manager/core/`: Business logic (TaskService).
- `src/task_manager/infra/`: Persistence logic (TaskRepository).
- `src/task_manager/models/`: Data models (Task).
- `tests/`: Unit tests.

## 🧪 Testing

Run tests with `pytest`:

```bash
pytest
```

## 🌗 Features

- Modern Dark Theme.
- Responsive design with scrollable task list.
