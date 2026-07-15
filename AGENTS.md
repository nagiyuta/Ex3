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
myproject/
├── manage.py
├── db.sqlite3
├── myproject/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/              # Main application
    ├── models.py       # Movie, Review models
    ├── views.py
    ├── admin.py
    └── migrations/
```

### Database models

- **Movie** — `title`, `director`, `release_year`, `genre`
- **Review** — `movie` (FK→Movie), `reviewer`, `rating`, `comment`, `created_at`

## Important project conventions

- Put business logic in `services.py`, not in views.
- Put reusable read/query logic in `selectors.py`.
- Follow Django best practices for model design and URL routing.

## Commands

- Run server: `cd myproject && python manage.py runserver`
- Run tests: `pytest`
- Create migrations: `cd myproject && python manage.py makemigrations`
- Apply migrations: `cd myproject && python manage.py migrate`

## Things that are easy to break

- Movie-Review ForeignKey relationship (CASCADE delete)
- Review rating validation (IntegerField)
- Query performance for movie reviews

## Change coupling

If you change:

- Movie model -> also check Review model, admin, and views
- Review model -> also check Movie related_name="reviews"
- Views -> also check URL conf

## Constraints

- Do not edit old migrations; create a new one instead.
- Do not rename API fields or URL names unless explicitly asked.
- Prefer small, targeted changes over broad refactors.

## Documentation use

- Use `openspec/specs/*` as the canonical source for technical/runtime documentation.
- For project-level conventions, examine the `context` section of `openspec/config.yaml`.
- For system-specific tasks, read the relevant capability spec under `openspec/specs/<capability>/spec.md`.
- Use `openspec/notes/*` as supplemental context only for non-normative ideas and backlog notes.
- Keep technical/runtime truth in `openspec/specs/*`; promote accepted ideas from notes into specs.
- Keep documentation up to date. If inconsistency between code and documentation is detected, report it to the user and suggest a fix.
- When a new feature is implemented or a certain fact about the system is discovered, suggest reflecting it in documentation.

## Testing expectations

Add or update tests for:

- Movie CRUD operations
- Review creation and validation
- Movie-Review relationship integrity
