# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2023-10-27

### Changed
- Refactored `TaskRepository` to use Strategy Pattern with `BaseRepository`.
- Improved GUI type hints for callbacks.
- Enhanced `TaskService` to depend on `BaseRepository` abstraction.
- Introduced `TaskFactory` in `models/task.py` for centralized task creation.
- Exposed `TaskApp` in `api/__init__.py`.

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
