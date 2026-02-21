# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2023-10-27

### Added
- `TaskFactory` in `models/task.py` to centralize task creation.
- `BaseRepository` abstract base class in `infra/repository.py` to implement the Strategy Pattern.
- New unit tests for `TaskFactory` in `tests/test_models.py`.

### Changed
- Refactored `TaskService` to use `BaseRepository` abstraction and `TaskFactory`.
- Updated existing tests to use the new abstractions.
- Improved code quality with automated linting and formatting.

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
