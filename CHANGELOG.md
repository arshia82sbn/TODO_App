# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2023-11-20

### Changed
- Implemented Factory Pattern with `TaskFactory` in `src/task_manager/models/task.py`.
- Implemented Strategy Pattern with `BaseRepository` in `src/task_manager/infra/repository.py`.
- Improved GUI type hints and cleaned up package API exports.
- Updated `pyproject.toml` with clearer dependency documentation and linting rules.

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
