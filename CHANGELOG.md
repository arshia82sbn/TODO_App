# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2024-03-27

### Added
- Implemented Factory Pattern with `TaskFactory` in `models/task.py`.
- Implemented Strategy Pattern with `BaseRepository` in `infra/repository.py`.
- Improved GUI type hints using `Callable` for callbacks.

### Changed
- Updated `TaskService` to use Dependency Inversion for its repository dependency.
- Refined `pyproject.toml` with clearer dependency documentation and improved `ruff` linting rules.
- Exported `TaskApp` in `api/__init__.py` for a cleaner public interface.

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
