# AGENTS.md

## Project scope

This is a Django app called **FilmReview** for viewing and writing movie reviews.

- Python 3.13+, Django 6.x
- Package manager: uv
- Formatter: black (line-length 88)
- Linter: pylint
- Test framework: pytest + pytest-cov
- Database: SQLite3

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
│       ├── views.py        # 5 view functions
│       ├── urls.py         # 5 URL patterns
│       ├── templates/      # HTML templates
│       ├── static/css/     # Stylesheets
│       ├── admin.py
│       ├── apps.py
│       └── migrations/
├── openspec/               # Project specifications
├── opencode.json           # OpenCode configuration
└── pyproject.toml          # Python dependencies
```

### Database models

- **User** — `username` (unique), `password`
- **Movie** — `title`, `poster_image`
- **Review** — `user` (FK→User), `movie` (FK→Movie), `star_rating`, `review_text`

### URL routes

| Path | View | Name | Status |
|------|------|------|--------|
| `/` | `home` | `home` | Implemented (template) |
| `/register/` | `register` | `register` | Implemented (stub) |
| `/login/` | `login` | `login` | Implemented (DB query) |
| `/movies/` | `movie_list` | `movie_list` | Implemented (stub) |
| `/review/<int:movie_id>/` | `review` | `review` | Implemented (stub) |

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
- Session management in login view
- Form validation logic in register/review views

## Change coupling

If you change:

- User model -> also check Review (FK), views, admin
- Movie model -> also check Review (FK), views, admin
- Review model -> also check views, admin
- Views -> also check URL conf and templates

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
- Movie listing
- Review creation and validation
