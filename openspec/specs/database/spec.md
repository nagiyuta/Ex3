# Database Design Specification

## Purpose

This specification defines the database schema for the FilmReview application, a Django-based system for user registration, movie browsing, and review writing.

## Technology

- **Engine**: SQLite3 (django.db.backends.sqlite3)
- **File**: `myproject/db.sqlite3`
- **ORM**: Django ORM
- **Primary keys**: BigAutoField (auto-generated)
- **Migrations**: 2 (0001_initial, 0002_alter_fields)

## Models

### User

Stores user accounts for the application.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `username` | CharField | max_length=30, unique=True | Login name |
| `password` | CharField | max_length=9 | Password (plain text) |

**String representation**: `User.username`

---

### Movie

Stores information about films.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `title` | CharField | max_length=200 | Movie title |
| `poster_image` | URLField | max_length=500, blank=True | Poster image URL |

**String representation**: `Movie.title`

**Note**: `poster_image` is optional (blank=True). Changed from CharField to URLField in migration 0002.

---

### Review

Stores user reviews linked to movies.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | BigAutoField | PRIMARY KEY, AUTO | Unique identifier |
| `user` | ForeignKey | →User, ON DELETE CASCADE, related_name="reviews" | Review author |
| `movie` | ForeignKey | →Movie, ON DELETE CASCADE, related_name="reviews" | Reviewed movie |
| `star_rating` | PositiveSmallIntegerField | — | Rating (0-32767) |
| `review_text` | TextField | — | Review content |

**String representation**: `"{movie.title} - {star_rating}/10"`

**Access patterns**:
- `movie.reviews.all()` — all reviews for a movie
- `user.reviews.all()` — all reviews by a user
- `review.user.username` — reviewer's name

## Relationships

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│     User     │       │    Review    │       │    Movie     │
├──────────────┤       ├──────────────┤       ├──────────────┤
│ id (PK)      │◄──┐   │ id (PK)      │   ┌──►│ id (PK)      │
│ username     │   └───│ user (FK)    │   │   │ title        │
│ password     │       │ movie (FK)───┘   │   │ poster_image │
└──────────────┘       │ star_rating  │   └───│ (URLField)   │
        │              │ review_text  │       └──────────────┘
        │              └──────────────┘
        │                                 
        └───────────── 1:N ──────────────┘
```

- **One User** has **many Reviews** (1:N via `user` FK, related_name="reviews")
- **One Movie** has **many Reviews** (1:N via `movie` FK, related_name="reviews")
- Deleting a User **cascades** to delete their Reviews
- Deleting a Movie **cascades** to delete its Reviews

## Derived Data

### Average Rating

Movies display an average rating calculated via Django ORM annotation:

```python
Movie.objects.annotate(average_rating=Avg("reviews__star_rating"))
```

This is NOT stored in the database — it is computed on each query.

## Requirements

### User Management

- The system SHALL allow creating users with unique username and password
- The system SHALL enforce username uniqueness
- The system SHALL allow retrieving users by ID or username

### Movie Management

- The system SHALL allow creating movies with title and optional poster image URL
- The system SHALL allow retrieving all movies
- The system SHALL allow retrieving a single movie by ID
- The system SHALL calculate average rating from reviews

### Review Management

- The system SHALL allow creating reviews linked to a user and movie
- The system SHALL allow retrieving all reviews for a movie (via related_name)
- The system SHALL allow retrieving all reviews by a user (via related_name)
- The system SHALL allow deleting reviews
- The system SHALL enforce foreign key constraints (CASCADE delete)

### Data Integrity

- The system SHALL enforce foreign key constraints between Review→User and Review→Movie
- The system SHALL use BigAutoField for all primary keys
- The system SHALL enforce unique usernames
