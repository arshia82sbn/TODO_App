# Daily Task Manager

A modern, professional desktop application for managing your daily tasks, built with Python and `customtkinter`.

## Features

- **Clean UI:** Modern dark-themed interface with scrollable task list.
- **Persistent Storage:** Tasks are automatically saved to a JSON file.
- **Architectural Excellence:** Implements Strategy, Factory, and Facade design patterns.
- **Type Safe:** Fully type-hinted and verified with `mypy`.
- **Quality Assured:** Comprehensive test suite and linting with `ruff`.

## Project Structure

- `src/task_manager/api/`: GUI implementation using `customtkinter`.
- `src/task_manager/core/`: Business logic and service interfaces.
- `src/task_manager/infra/`: Data persistence (JSON repository).
- `src/task_manager/models/`: Core data classes and factories.

## Installation

```bash
pip install .
```

## Usage

Run the application using the command-line entry point:

```bash
task-manager
```

Or directly via Python:

```bash
python -m task_manager
```

## Development

Install development dependencies:

```bash
pip install ".[dev]"
```

### Running Tests

```bash
pytest
```

### Linting and Type Checking

```bash
ruff check .
mypy src
```
