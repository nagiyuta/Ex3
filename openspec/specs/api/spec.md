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
| **Response** | `HttpResponse("Film Review Home")` |

### User Registration

| Property | Value |
|----------|-------|
| **Path** | `/register/` |
| **View** | `views.register` |
| **Name** | `register` |
| **Method** | GET |
| **Response** | `HttpResponse("User Registration Page")` |

### Movie List

| Property | Value |
|----------|-------|
| **Path** | `/movies/` |
| **View** | `views.movie_list` |
| **Name** | `movie_list` |
| **Method** | GET |
| **Response** | `HttpResponse("Movie List")` |

### Search Movies

| Property | Value |
|----------|-------|
| **Path** | `/movies/search/` |
| **View** | `views.search_movies` |
| **Name** | `search_movies` |
| **Method** | GET |
| **Response** | `HttpResponse("Search Movies")` |

### Sort Movies

| Property | Value |
|----------|-------|
| **Path** | `/movies/sort/` |
| **View** | `views.sort_movies` |
| **Name** | `sort_movies` |
| **Method** | GET |
| **Response** | `HttpResponse("Sort Movies by Star Rating")` |

### Filter Movies

| Property | Value |
|----------|-------|
| **Path** | `/movies/filter/` |
| **View** | `views.filter_movies` |
| **Name** | `filter_movies` |
| **Method** | GET |
| **Response** | `HttpResponse("Hide Movies Below Selected Rating")` |

### Movie Detail

| Property | Value |
|----------|-------|
| **Path** | `/movies/<int:movie_id>/` |
| **View** | `views.movie_detail` |
| **Name** | `movie_detail` |
| **Method** | GET |
| **Parameters** | `movie_id` (int) |
| **Response** | `HttpResponse("Movie {movie_id}")` |

### Write Review

| Property | Value |
|----------|-------|
| **Path** | `/movies/<int:movie_id>/review/` |
| **View** | `views.write_review` |
| **Name** | `write_review` |
| **Method** | GET |
| **Parameters** | `movie_id` (int) |
| **Response** | `HttpResponse("Write Review for Movie {movie_id}")` |

## Current State

All views are **stubs** returning plain text responses. No template rendering, form handling, or ORM queries are implemented yet.

## Requirements

### Home

- The system SHALL display a home page at the root URL

### User Registration

- The system SHALL display a registration page at `/register/`

### Movie Browsing

- The system SHALL list all movies at `/movies/`
- The system SHALL display movie details at `/movies/<id>/`
- The system SHALL support searching movies at `/movies/search/`
- The system SHALL support sorting movies by rating at `/movies/sort/`
- The system SHALL support filtering movies by rating at `/movies/filter/`

### Review Writing

- The system SHALL allow writing reviews at `/movies/<id>/review/`
