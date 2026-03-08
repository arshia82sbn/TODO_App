# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2023-10-28

### Added
- Factory Pattern implementation for Task creation.
- Strategy Pattern implementation for data persistence.
- Improved GUI type hints and public API exposure.

### Changed
- Refactored `TaskRepository` to `JsonTaskRepository` using an abstract base class.
- Updated `pyproject.toml` with stricter linting rules and version bump.

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
