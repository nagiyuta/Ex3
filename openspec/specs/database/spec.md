# Database Design Specification

## Purpose

This specification defines the database schema for the FilmReview application, a Django-based system for user registration, movie browsing, and review writing.

## Technology

- **Engine**: SQLite3 (django.db.backends.sqlite3)
- **File**: `myproject/db.sqlite3`
- **ORM**: Django ORM
- **Primary keys**: BigAutoField (auto-generated)

## Models

### User

Stores user accounts for the application.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `username` | CharField | max_length=30, unique=True | Login name |
| `password` | CharField | max_length=9 | Password (plain text) |

**String representation**: `User.username`

### Movie

Stores information about films.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `title` | CharField | max_length=200 | Movie title |
| `poster_image` | CharField | max_length=255 | Poster image URL or path |

**String representation**: `Movie.title`

### Review

Stores user reviews linked to movies.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `user` | ForeignKey | →User, ON DELETE CASCADE | Review author |
| `movie` | ForeignKey | →Movie, ON DELETE CASCADE | Reviewed movie |
| `star_rating` | PositiveSmallIntegerField | — | Rating (0-32767) |
| `review_text` | TextField | — | Review content |

**String representation**: `"{movie.title} - {star_rating}/10"`

## Relationships

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│     User     │       │    Review    │       │    Movie     │
├──────────────┤       ├──────────────┤       ├──────────────┤
│ id (PK)      │◄──┐   │ id (PK)      │   ┌──►│ id (PK)      │
│ username     │   └───│ user (FK)    │   │   │ title        │
│ password     │       │ movie (FK)───┘   │   │ poster_image │
└──────────────┘       │ star_rating  │   │   └──────────────┘
        │              │ review_text  │   │
        │              └──────────────┘   │
        │                                 │
        └───────────── 1:N ──────────────┘
```

- **One User** has **many Reviews** (1:N via `user` FK)
- **One Movie** has **many Reviews** (1:N via `movie` FK)
- Deleting a User **cascades** to delete their Reviews
- Deleting a Movie **cascades** to delete its Reviews

## Requirements

### User Management

- The system SHALL allow creating users with unique username and password
- The system SHALL enforce username uniqueness
- The system SHALL allow retrieving users by ID or username

### Movie Management

- The system SHALL allow creating movies with title and poster image
- The system SHALL allow retrieving all movies
- The system SHALL allow retrieving a single movie by ID

### Review Management

- The system SHALL allow creating reviews linked to a user and movie
- The system SHALL allow retrieving all reviews for a movie
- The system SHALL allow retrieving all reviews by a user
- The system SHALL allow deleting reviews
- The system SHALL enforce foreign key constraints (CASCADE delete)

### Data Integrity

- The system SHALL enforce foreign key constraints between Review→User and Review→Movie
- The system SHALL use BigAutoField for all primary keys
- The system SHALL enforce unique usernames
