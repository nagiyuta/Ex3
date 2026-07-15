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

**POST**: Validates and saves user.
- `username` — required, max 30 characters, must be unique
- `password` — required, max 9 characters
- Creates `User` object on success
- Returns 400 on validation error or duplicate username

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
- Returns 400 on `User.DoesNotExist`

---

### Movie List

| Property | Value |
|----------|-------|
| **Path** | `/movies/` |
| **View** | `views.movie_list` |
| **Name** | `movie_list` |
| **Method** | GET |
| **Template** | `movie_list.html` |

Renders movie list with search, filter, sort, and pagination.

**Query parameters:**
- `search` — title search (icontains)
- `rating` — minimum average rating (0-10)
- `sort` — "title" (default), "rating_desc", "rating_asc"
- `page` — pagination page number

**Features:**
- Annotates movies with `average_rating` from reviews
- Paginates results (10 per page)
- HTMX-enabled for live search

---

### Movie Search (HTMX Partial)

| Property | Value |
|----------|-------|
| **Path** | `/movies/search/` |
| **View** | `views.movie_search` |
| **Name** | `movie_search` |
| **Method** | GET |
| **Template** | `partials/movie_results.html` |

Returns HTML fragment for HTMX dynamic search.

**Query parameters:**
- `search` — title search (icontains)
- `rating` — minimum average rating (0-10)

**Returns:** Partial HTML with movie list items.

---

### Movie Detail

| Property | Value |
|----------|-------|
| **Path** | `/movies/<int:movie_id>/` |
| **View** | `views.movie_detail` |
| **Name** | `movie_detail` |
| **Method** | GET |
| **Template** | `movie_detail.html` |
| **Parameters** | `movie_id` (int) |

Displays movie details with reviews.

**Context:**
- `movie` — Movie object with `average_rating` annotation
- `reviews` — QuerySet of reviews with `select_related("user")`

**Returns 404** if movie not found.

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

**GET**: Renders review form for the movie.

**POST**: Validates and saves review.
- Requires `request.session["user_id"]` (login required)
- `rating` — required, integer, 0-10
- `review` — required, non-empty
- Creates `Review` object on success
- Redirects to `movie_detail` on success
- Returns 400 on validation error
- Returns 403 if not logged in

## Current State

| View | DB Operations | Status |
|------|--------------|--------|
| `home` | None | Implemented |
| `register` | Creates User | Implemented |
| `login` | Queries User | Implemented |
| `movie_list` | Queries Movies + Avg | Implemented |
| `movie_search` | Queries Movies + Avg | Implemented |
| `movie_detail` | Queries Movie + Reviews | Implemented |
| `review` | Creates Review | Implemented |

## Requirements

### Home

- The system SHALL display a home page at the root URL

### User Registration

- The system SHALL display a registration form at `/register/`
- The system SHALL validate username (required, max 30 chars, unique)
- The system SHALL validate password (required, max 9 chars)
- The system SHALL save new users to the database

### User Login

- The system SHALL display a login form at `/login/`
- The system SHALL authenticate users against the database
- The system SHALL create a session on successful login
- The system SHALL display an error for invalid credentials

### Movie Browsing

- The system SHALL list movies at `/movies/` with average rating
- The system SHALL support searching movies by title (icontains)
- The system SHALL support filtering movies by minimum average rating
- The system SHALL support sorting by title or rating
- The system SHALL paginate results (10 per page)
- The system SHALL display movie details at `/movies/<id>/`

### Review Writing

- The system SHALL display a review form at `/review/<id>/`
- The system SHALL require login to submit a review
- The system SHALL validate rating (required, 0-10)
- The system SHALL validate review text (required, non-empty)
- The system SHALL save reviews to the database
- The system SHALL redirect to movie detail after submission
