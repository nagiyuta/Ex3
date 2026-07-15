# AGENTS.md

## Project scope

This is a Django app called **FilmReview** for viewing and writing movie reviews.

- Python 3.13+, Django 6.x
- Package manager: uv
- Formatter: black (line-length 88)
- Linter: pylint
- Test framework: pytest + pytest-cov
- Database: SQLite3
- Frontend: htmx 2.0.4 (for dynamic search)

### Project structure

```
app/
├── myproject/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── myproject/          # Project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── myapp/              # Main application
│       ├── models.py       # User, Movie, Review models
│       ├── views.py        # 8 view functions
│       ├── urls.py         # 7 URL patterns
│       ├── admin.py        # All models registered
│       ├── templates/      # HTML templates + partials
│       ├── static/css/     # Stylesheets
│       └── migrations/
├── openspec/               # Project specifications
├── opencode.json           # OpenCode configuration
└── pyproject.toml          # Python dependencies
```

### Database models

- **User** — `username` (unique), `password`
- **Movie** — `title`, `poster_image` (URLField, optional)
- **Review** — `user` (FK→User), `movie` (FK→Movie), `star_rating`, `review_text`

### URL routes

| Path | View | Name | Status |
|------|------|------|--------|
| `/` | `home` | `home` | Template render |
| `/register/` | `register` | `register` | DB save + validation |
| `/login/` | `login` | `login` | DB query + session |
| `/movies/` | `movie_list` | `movie_list` | DB query + pagination + HTMX |
| `/movies/search/` | `movie_search` | `movie_search` | Partial HTML (HTMX) |
| `/movies/<id>/` | `movie_detail` | `movie_detail` | DB query + reviews |
| `/review/<id>/` | `review` | `review` | DB save + validation |

## Important project conventions

- Follow Django best practices for model design and URL routing.
- Do not edit old migrations; create a new one instead.
- Prefer small, targeted changes over broad refactors.

## Commands

- Run server: `cd myproject && python manage.py runserver`
- Run tests: `pytest`
- Create migrations: `cd myproject && python manage.py makemigrations`
- Apply migrations: `cd myproject && python manage.py migrate`

## Things that are easy to break

- User-Movie-Review foreign key relationships (CASCADE delete)
- star_rating validation (PositiveSmallIntegerField, 0-32767)
- Session management (user_id in session)
- HTMX partial responses (movie_search view)
- Pagination logic in movie_list

## Change coupling

If you change:

- User model -> also check Review (FK), views, admin
- Movie model -> also check Review (FK), views, admin, templates
- Review model -> also check views, admin, templates
- Views -> also check URL conf, templates, partials
- Templates -> also check view context variables

## Constraints

- Do not edit old migrations; create a new one instead.
- Do not rename URL names unless explicitly asked.
- Prefer small, targeted changes over broad refactors.

## Documentation use

- Use `openspec/specs/*` as the canonical source for technical/runtime documentation.
- For project-level conventions, examine the `context` section of `openspec/config.yaml`.
- For system-specific tasks, read the relevant capability spec under `openspec/specs/<capability>/spec.md`.
- Keep documentation up to date. If inconsistency between code and documentation is detected, report it to the user and suggest a fix.

## Testing expectations

Add or update tests for:

- User registration and login
- Movie listing, search, and detail views
- Review creation and validation
- Pagination and filtering
