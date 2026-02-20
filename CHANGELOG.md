# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2024-05-22

### Added
- TaskFactory to centralize task creation (Factory Pattern).
- BaseRepository abstract class for pluggable storage (Strategy Pattern).
- New unit tests for TaskFactory.

### Changed
- Refactored TaskService to use TaskFactory and depend on BaseRepository abstraction.
- Improved code formatting and linting compliance.

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
