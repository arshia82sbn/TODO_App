# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2023-10-28

### Changed
- Implemented Factory Pattern with `TaskFactory` in `models/task.py`.
- Implemented Strategy Pattern with `BaseRepository` in `infra/repository.py`.
- Improved GUI type hints with `Callable`.
- Exported `TaskApp` in `api/__init__.py`.
- Updated dependencies with comments in `pyproject.toml`.

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
