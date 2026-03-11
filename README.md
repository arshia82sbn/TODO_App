# Daily Task Manager

A modern and professional daily task manager built with Python and CustomTkinter.

## Features

- **Class-based GUI**: Clean and intuitive interface using `customtkinter`.
- **Repository Pattern**: Abstracted data storage for easy extension.
- **Service Layer**: Decoupled business logic from UI and infrastructure.
- **Factory Pattern**: Centralized object creation.
- **Modern Build System**: Managed with `pyproject.toml` and `hatchling`.
- **Quality Assured**: Full type hints, PEP 8 compliance, and comprehensive unit tests.

## Installation

```bash
pip install .
```

## Usage

Run the application using the CLI entry point:

```bash
task-manager
```

Or run it as a module:

```bash
python -m task_manager
```

## Development

Install development dependencies:

```bash
pip install ".[dev]"
```

Run tests:

```bash
pytest
```

Run linting:

```bash
ruff check .
```

Run type checking:

```bash
mypy src
```
