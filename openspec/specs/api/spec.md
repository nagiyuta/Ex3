# API Specification

## Purpose

This specification defines the URL routes and view functions for the FilmReview application.

## URL Configuration

The project uses two-level URL configuration:
- `myproject/urls.py` — includes `myapp.urls`
- `myapp/urls.py` — defines all application routes

## Routes

### Home

| Property | Value |
|----------|-------|
| **Path** | `/` |
| **View** | `views.home` |
| **Name** | `home` |
| **Method** | GET |
| **Template** | `home.html` |

Renders the home page template.

---

### User Registration

| Property | Value |
|----------|-------|
| **Path** | `/register/` |
| **View** | `views.register` |
| **Name** | `register` |
| **Methods** | GET, POST |
| **Template** | `register.html` |

**GET**: Renders registration form.

**POST**: Validates input fields.
- `username` — required, max 30 characters
- `password` — required, max 9 characters

Returns validation errors or success response. Does NOT save to database yet (stub).

---

### User Login

| Property | Value |
|----------|-------|
| **Path** | `/login/` |
| **View** | `views.login` |
| **Name** | `login` |
| **Methods** | GET, POST |
| **Template** | `login.html` |

**GET**: Renders login form.

**POST**: Authenticates user.
- Queries `User.objects.get(username, password)`
- Sets `request.session["user_id"]` on success
- Returns error on `User.DoesNotExist`

---

### Movie List

| Property | Value |
|----------|-------|
| **Path** | `/movies/` |
| **View** | `views.movie_list` |
| **Name** | `movie_list` |
| **Method** | GET |
| **Template** | `movie_list.html` |

Renders movie list template. Accepts query parameters:
- `search` — search keyword (not yet implemented)
- `rating` — minimum rating filter (not yet implemented)

Movie list is currently hardcoded in template.

---

### Write Review

| Property | Value |
|----------|-------|
| **Path** | `/review/<int:movie_id>/` |
| **View** | `views.review` |
| **Name** | `review` |
| **Methods** | GET, POST |
| **Template** | `review.html` |
| **Parameters** | `movie_id` (int) |

**GET**: Renders review form.

**POST**: Validates review input.
- `rating` — required, integer, 0-10
- `review` — required, non-empty

Returns validation errors or confirmation. Does NOT save to database yet (stub).

## Current State

| View | Status |
|------|--------|
| `home` | Implemented (template render) |
| `register` | Stub (validation only, no DB save) |
| `login` | Implemented (DB query + session) |
| `movie_list` | Stub (hardcoded data) |
| `review` | Stub (validation only, no DB save) |

## Requirements

### Home

- The system SHALL display a home page at the root URL

### User Registration

- The system SHALL display a registration form at `/register/`
- The system SHALL validate username (required, max 30 chars)
- The system SHALL validate password (required, max 9 chars)
- The system SHALL save new users to the database

### User Login

- The system SHALL display a login form at `/login/`
- The system SHALL authenticate users against the database
- The system SHALL create a session on successful login
- The system SHALL display an error for invalid credentials

### Movie Browsing

- The system SHALL list movies at `/movies/`
- The system SHALL support searching movies by keyword
- The system SHALL support filtering movies by minimum rating

### Review Writing

- The system SHALL display a review form at `/review/<id>/`
- The system SHALL validate rating (required, 0-10)
- The system SHALL validate review text (required, non-empty)
- The system SHALL save reviews to the database
