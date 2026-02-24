# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2023-10-27

### Added
- Initial refactored release.
- Class-based GUI using `customtkinter`.
- Repository pattern for task persistence with `BaseRepository` abstraction (Strategy Pattern).
- `TaskFactory` for centralized task creation (Factory Pattern).
- Service layer for business logic acting as a Facade.
- Full type hints and Google-style docstrings throughout.
- `pyproject.toml` for modern build system.
- Comprehensive unit tests with `pytest` (core, infra, and models).
- CI workflow with GitHub Actions for linting, type-checking, and testing.
