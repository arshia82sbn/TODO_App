# ✅ Daily Task Manager

A professional, refactored task manager built with **CustomTkinter**.

![Todo App](demo.gif)

## 🚀 Features

- ➕ **Add Tasks**: Easily enter new tasks.
- ✅ **Toggle Tasks**: Mark tasks as completed with a visual strike-through.
- ❌ **Delete Tasks**: Remove tasks instantly.
- 💾 **Persistence**: Automatic saving to `tasks.json`.
- 🏗️ **Clean Architecture**: Implemented with Repository and Service patterns.
- 🧪 **Tested**: Unit tests included.

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

- `src/task_manager/api/`: GUI implementation.
- `src/task_manager/core/`: Business logic and interfaces.
- `src/task_manager/infra/`: Persistence implementations.
- `src/task_manager/models/`: Data models and factories.
- `tests/`: Unit tests.

## 🛠️ Architecture & Design Patterns

- **Factory Pattern**: `TaskFactory` centralizes task creation.
- **Repository Pattern**: `BaseRepository` provides a pluggable persistence interface.
- **Strategy Pattern**: Different repository implementations can be used.
- **Facade Pattern**: `TaskService` simplifies interaction between UI and core logic.

## 🧪 Testing

Run tests with `pytest`:

```bash
pytest
```

## 🌗 Features

- Modern Dark Theme.
- Responsive design with scrollable task list.
