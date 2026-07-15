# Templates Specification

## Purpose

This specification defines the HTML templates for the FilmReview application.

## Template Structure

All templates are located in `myproject/myapp/templates/` and use Django's template inheritance system with htmx for dynamic content.

## Base Template

### base.html

The base layout template that all other templates extend.

**Features:**
- HTML5 doctype
- Static CSS loading (`css/style.css`)
- Navigation bar with links to: Home, Movies, Register, Login
- Content block for child templates
- htmx 2.0.4 loaded via CDN

**Navigation links:**
- Home → `/`
- Movies → `/movies/`
- Register → `/register/`
- Login → `/login/`

## Page Templates

### home.html

Extends `base.html`. Displays a welcome message.

**Content:**
- Heading: "Welcome!"
- Paragraph: "Welcome to Film Review. Search movies and write reviews."

---

### register.html

Extends `base.html`. User registration form.

**Form:**
- Method: POST
- Fields:
  - `username` — text input
  - `password` — password input
- CSRF token included
- Submit button: "Register"

---

### login.html

Extends `base.html`. User login form.

**Form:**
- Method: POST
- Fields:
  - `username` — text input
  - `password` — password input
- CSRF token included
- Submit button: "Login"

---

### movie_list.html

Extends `base.html`. Movie list with HTMX-powered live search.

**Features:**
- Search form with HTMX integration:
  - `hx-get` → `/movies/search/`
  - `hx-target` → `#movie-results`
  - `hx-trigger` → keyup with 500ms delay, change on rating
  - `hx-include` → search and rating inputs
- Sort dropdown (title, highest rating, lowest rating)
- Pagination controls (Previous/Next, page X of Y)
- Results section with `id="movie-results"`

**Form fields:**
- `search` — text input (search keyword)
- `rating` — number input (min 0, max 10)
- `sort` — select dropdown

---

### movie_detail.html

Extends `base.html`. Movie detail page with reviews.

**Content:**
- Movie title heading
- Poster image (if available)
- Average rating display (formatted to 1 decimal)
- Reviews list with username and rating
- "Write a review" link
- "Back to movie list" link

---

### review.html

Extends `base.html`. Review writing form.

**Form:**
- Method: POST
- Fields:
  - `rating` — number input (min 0, max 10, required)
  - `review` — textarea (6 rows, required)
- CSRF token included
- Submit button: "Submit Review"
- "Back to movie details" link

## Partial Templates

### partials/movie_results.html

HTMX partial for dynamic movie search results.

**Features:**
- Displays movie list with poster images
- Shows average rating (formatted to 1 decimal) or "No ratings"
- Links to movie detail page
- "No matching movies" message when empty

## Static Files

### css/style.css

Styling for the application.

**Features:**
- Arial font family
- Light gray background (#f4f4f4)
- Dark blue headings (#2c3e50, #34495e)
- Blue links (#0066cc) with red hover
- White form backgrounds with rounded corners
- Responsive design (max-width: 600px)
- Movie list styling (white cards, bold links)
- Movie detail layout (max-width 800px, centered)
- Review list styling (white cards)
- Poster images (250px width, rounded corners)

## Requirements

### Base Template

- The system SHALL provide a consistent layout across all pages
- The system SHALL include navigation links to main sections
- The system SHALL load static CSS files
- The system SHALL include htmx 2.0.4

### Forms

- All forms SHALL include CSRF tokens
- All forms SHALL use proper input types (text, password, number)
- All forms SHALL have submit buttons

### HTMX Integration

- Movie list search SHALL use HTMX for live updates
- Search results SHALL update without page reload
- Results section SHALL have polite aria-live for accessibility

### Responsive Design

- The system SHALL be usable on mobile devices
- Navigation SHALL stack vertically on small screens
