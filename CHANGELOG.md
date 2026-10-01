# Changelog

All notable changes to this project are documented in this file.

This changelog is generated from the repository git history and follows a Keep a Changelog-inspired structure.

## [Unreleased]

### Added
- Student registration form enhancements with an email field and improved labels.
- Delete-student functionality with backend API support and user-friendly error handling.
- Email support in the student model and data representation (`email_id`).
- Frontend support for loading, creating, updating, and removing student records.
- Initial frontend UI structure, JavaScript interactions, and CORS support for local development.
- Initial FastAPI-based student management API and core data model.

### Changed
- Reorganized frontend HTML layout for better readability and consistency.
- Improved frontend styling and header consistency across the student registry UI.
- Updated the mark update flow and integrated HTML controls with JavaScript behavior.
- Refined API routing and subject comparison logic for student mark updates.
- Enhanced data model and API behavior around student registration and record management.

### Fixed
- Corrected the use of `Field(default_factory=...)` for student marks values.
- Fixed router prefix configuration in the main application.
- Corrected API endpoint paths and improved validation logic.
- Improved delete-student error handling and API reliability.
- Cleaned up repository state and ignored generated files.

## [0.1.0] - 2026-09-14

### Added
- Initial implementation of the Mark Registry Web API with student management features.
- Basic FastAPI routes for creating, updating, and listing student records.
- Initial frontend interface for the student registry.

### Changed
- Improved licensing metadata and repository housekeeping.

### Fixed
- Corrected app startup and routing issues during initial setup.

---

### Recent commit history

- `7bdf8df` - feat: enhance student registration form with email field and improved labels
- `edc2e76` - feat: include email_id in create_students function for student registration
- `2597889` - feat: add email_id field to Student model for enhanced data representation
- `1b27084` - feat: implement delete student functionality with improved error handling
- `9ffce7f` - refactor: reorganize HTML structure for better readability and consistency
- `10a5065` - feat: implement delete student API endpoint with proper error handling
- `c2d2de8` - feat(html): add new remove layout display html and wire script.js
- `7ff2c6d` - feat: defined remove function in routes to add a student remove API
- `bdd3693` - refactor: UI enhancements for frontend consistency
- `f690e90` - feat: wired HTML to script.js for marks updating feature
- `4cfbe5c` - feat: add function to update student marks by ID
- `95398e1` - feat: implement student loading and creation functions in script.js
- `52a3902` - feat: create initial index.html file for student registry interface
- `dd6f6a0` - feat: add CORS middleware to enable cross-origin requests
- `60d6eea` - feat: add script.js file for frontend functionality
- `2dde149` - feat: add initial index.html file for frontend structure
- `ce8fe0c` - fix: use Field with default_factory for marks in Student model
- `3c571a7` - fix: add prefix to student router in main application
- `4c1af92` - fix: correct endpoint path and improve subject comparison in add_or_update_mark function
- `cc345d9` - chore: update .gitignore to include app/data.json and adjust pycache patterns
- `1994388` - chore: remove unused data.json file
- `dab527b` - refactor: added correct name copyright owner in licence
- `20adcbd` - Implement Mark Registry Web API with student management features
- `1173a58` - Add initial implementation of FastAPI student management system
- `8a188e2` - Initial commit
