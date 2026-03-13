# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2023-10-27

### Added
- Strategy Pattern for repository persistence via `BaseRepository`.
- Factory Pattern for task creation via `TaskFactory`.
- Dependency injection in `__main__.py`.
- Improved type hints and docstrings across all modules.
- Explicit UTF-8 encoding for file I/O.

### Changed
- Refactored `TaskService` to depend on `BaseRepository` interface.
- Updated `TaskApp` to require a `TaskService` instance.
- Enhanced `pyproject.toml` with stricter linting (ruff) and type checking (mypy) rules.

## [0.1.0] - 2023-10-27

### Added
- Initial refactored release.
- Class-based GUI using `customtkinter`.
- Repository pattern for task persistence.
- Service layer for business logic.
- Type hints and docstrings throughout.
- `pyproject.toml` for modern build system.
- Basic unit tests with `pytest`.
- CI workflow with GitHub Actions.
