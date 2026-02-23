# ✅ Daily Task Manager

A professional, refactored task manager built with **CustomTkinter**.

![Todo App](demo.gif)

## 🚀 Features

- ➕ **Add Tasks**: Easily enter new tasks.
- ✅ **Toggle Tasks**: Mark tasks as completed with a visual strike-through.
- ❌ **Delete Tasks**: Remove tasks instantly.
- 💾 **Persistence**: Automatic saving to `tasks.json`.
- 🏗️ **Clean Architecture**: Implemented with Repository, Factory, and Service patterns.
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

- `src/task_manager/api/`: Public interface and GUI.
- `src/task_manager/core/`: Business logic (TaskService).
- `src/task_manager/infra/`: Persistence logic (TaskRepository).
- `src/task_manager/models/`: Data models (Task) and Factories.
- `tests/`: Unit tests.

## 🧪 Testing

Run tests with `pytest`:

```bash
pytest
```

## 🌗 Features

- Modern Dark Theme.
- Responsive design with scrollable task list.
