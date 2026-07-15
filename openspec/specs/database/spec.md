# Database Design Specification

## Purpose

This specification defines the database schema for the FilmReview application, a Django-based system for managing movies and user reviews.

## Technology

- **Engine**: SQLite3 (django.db.backends.sqlite3)
- **File**: `myproject/db.sqlite3`
- **ORM**: Django ORM
- **Primary keys**: BigAutoField (auto-generated)

## Models

### Movie

Stores information about films.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `title` | CharField | max_length=200 | Movie title |
| `director` | CharField | max_length=100 | Director name |
| `release_year` | IntegerField | — | Year of release |
| `genre` | CharField | max_length=100 | Genre category |

**String representation**: `Movie.title`

### Review

Stores user reviews linked to movies.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `movie` | ForeignKey | →Movie, ON DELETE CASCADE | Associated movie |
| `reviewer` | CharField | max_length=100 | Reviewer name |
| `rating` | IntegerField | — | Rating score |
| `comment` | TextField | — | Review text |
| `created_at` | DateTimeField | auto_now_add=True | Creation timestamp |

**String representation**: `"{movie.title} - {reviewer}"`

**Related name**: `reviews` (access via `movie.reviews.all()`)

## Relationships

```
┌──────────────┐       ┌──────────────┐
│    Movie     │       │    Review    │
├──────────────┤       ├──────────────┤
│ id (PK)      │◄──────│ id (PK)      │
│ title        │   1:N │ movie (FK)   │
│ director     │       │ reviewer     │
│ release_year │       │ rating       │
│ genre        │       │ comment      │
└──────────────┘       │ created_at   │
                       └──────────────┘
```

- **One Movie** has **many Reviews** (1:N relationship)
- Deleting a Movie **cascades** to delete all its Reviews
- Reviews are accessible via `movie.reviews.all()`

## Requirements

### Movie Management

- The system SHALL allow creating movies with title, director, year, and genre
- The system SHALL allow retrieving all movies
- The system SHALL allow retrieving a single movie by ID
- The system SHALL allow updating movie information
- The system SHALL allow deleting movies (cascades to reviews)

### Review Management

- The system SHALL allow creating reviews linked to a movie
- The system SHALL allow retrieving all reviews for a movie
- The system SHALL allow retrieving a single review by ID
- The system SHALL allow deleting reviews
- The system SHALL automatically set `created_at` on review creation

### Data Integrity

- The system SHALL enforce foreign key constraints (CASCADE delete)
- The system SHALL use BigAutoField for all primary keys
- The system SHALL preserve referential integrity between Movie and Review
