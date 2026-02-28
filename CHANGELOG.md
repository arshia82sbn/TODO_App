# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2024-05-22

### Added
- `TaskFactory` for centralized task creation (Factory Pattern).
- `BaseRepository` abstract base class (Strategy Pattern).
- Exported `TaskApp` in `task_manager.api`.

### Changed
- Refactored `TaskService` to use Dependency Inversion with `BaseRepository`.
- Improved type hints in GUI layer.
- Cleaned up source code comments and docstrings.

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
