# AGENTS.md

## Project scope

This is a Django app called **FilmReview** for viewing and writing movie reviews.

- Python 3.13+, Django 6.x
- Package manager: uv
- Formatter: black (line-length 88)
- Linter: pylint
- Test framework: pytest + pytest-cov

## Important project conventions

- Put business logic in `services.py`, not in views or serializers.
- Put reusable read/query logic in `selectors.py`.
- Keep Celery tasks thin (if Celery is used); they should call service functions.
- Follow Django best practices for model design and URL routing.

## Commands

- Run server: `python manage.py runserver`
- Run tests: `pytest`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`

## Things that are easy to break

- API response shapes in API endpoints
- Model relationships and query performance
- Form validation logic

## Change coupling

If you change:

- a model -> also check serializers, factories, and admin
- views -> also check URL conf and templates
- permissions -> also check both web views and API endpoints

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

- Model changes
- API response changes
- Permission changes

## GitHub integration

This project uses OpenCode GitHub integration for automated code review and issue management.

### GitHub Actions workflows

- `.github/workflows/opencode.yml` - Responds to `/opencode` or `/oc` commands in issues and PR comments
- `.github/workflows/opencode-review.yml` - Automatically reviews PRs when opened or updated
- `.github/workflows/opencode-triage.yml` - Triages new issues automatically

### GitHub MCP server

The `github-manager` agent has access to GitHub MCP tools for local development. Use it to:

- List and read issues: `list_issues`, `get_issue`
- Create and update issues: `create_issue`, `update_issue`
- List and read PRs: `list_pull_requests`, `get_pull_request`
- Review code: `create_pull_request_review`
- Manage labels and comments

### Setup requirements

Set the following environment variables or GitHub repository secrets:

- `ANTHROPIC_API_KEY` - API key for the LLM provider
- `GITHUB_TOKEN` - GitHub personal access token (for MCP server)

### Usage examples

In GitHub comments (issues/PRs):

```
/opencode fix this issue
/oc review this PR
```

Locally (in OpenCode TUI):

```
@github-manager list open issues
@github-manager create a PR for the current branch
```
