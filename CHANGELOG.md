# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2023-10-27

### Changed
- Implemented Factory Pattern with `TaskFactory` for centralized task creation.
- Introduced `BaseRepository` abstract base class to implement Strategy Pattern for persistence.
- Refactored `TaskService` to use `TaskFactory` and depend on `BaseRepository`.
- Improved type hints in GUI layer by using explicit `Callable` types for callbacks.
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
