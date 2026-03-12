# Changelog

All notable changes to this project will be documented in this file.

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

## [0.1.1] - 2023-10-27

### Changed
- Implemented Factory Pattern for task creation via `TaskFactory`.
- Implemented Strategy Pattern for task persistence via `BaseRepository`.
- Refactored `TaskService` to use Dependency Inversion Principle.
- Decoupled core business logic from infrastructure implementations.
- Improved GUI documentation and type hinting.
