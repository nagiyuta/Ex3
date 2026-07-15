# Templates Specification

## Purpose

This specification defines the HTML templates for the FilmReview application.

## Template Structure

All templates are located in `myproject/myapp/templates/` and use Django's template inheritance system.

## Base Template

### base.html

The base layout template that all other templates extend.

**Features:**
- HTML5 doctype
- Static CSS loading (`css/style.css`)
- Navigation bar with links to: Home, Movies, Register, Login
- Content block for child templates

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

Extends `base.html`. Movie list with search/filter form.

**Form:**
- Method: GET
- Fields:
  - `search` — text input (search keyword)
  - `rating` — number input (min 0, max 10)
- Submit button: "Search"

**Movie list:**
- Currently hardcoded:
  - Inception
  - Interstellar
  - The Dark Knight

---

### review.html

Extends `base.html`. Review writing form.

**Form:**
- Method: POST
- Fields:
  - `rating` — number input (min 0, max 10)
  - `review` — textarea (5 rows, 40 cols)
- CSRF token included
- Submit button: "Submit"

## Static Files

### css/style.css

Basic styling for the application.

**Features:**
- Arial font family
- Light gray background (#f4f4f4)
- Dark blue headings (#2c3e50, #34495e)
- Blue links (#0066cc) with red hover
- White form backgrounds with rounded corners
- Responsive design (max-width: 600px)

## Requirements

### Base Template

- The system SHALL provide a consistent layout across all pages
- The system SHALL include navigation links to main sections
- The system SHALL load static CSS files

### Forms

- All forms SHALL include CSRF tokens
- All forms SHALL use proper input types (text, password, number)
- All forms SHALL have submit buttons

### Responsive Design

- The system SHALL be usable on mobile devices
- Navigation SHALL stack vertically on small screens
