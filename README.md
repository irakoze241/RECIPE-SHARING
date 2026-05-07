#  RecipeShare — A Recipe Sharing Platform

A clean, full-stack web application built with Python and Django that allows users to create, upload, and browse recipes with images. Designed as a student portfolio project with professional structure and real functionality.

---

# Features

| Feature | Description |
|---|---|
|  **User Authentication** | Register, log in, and log out using Django's built-in auth |
|  **Create Recipes** | Upload recipes with title, description, ingredients, instructions, and a photo |
|  **Image Upload** | Store and display recipe images via Django's media system |
|  **Search** | Search recipes by title or description keyword |
|  **Recipe Detail** | Full detail page with ingredients and numbered instructions |
|  **Edit / Delete** | Authors can edit or delete their own recipes |
|  **My Recipes Dashboard** | Each user has a personal dashboard to manage their recipes |
|  **Security** | CSRF protection, login-required views, author-only edit/delete |
|  **Responsive Design** | Mobile-friendly Bootstrap 5 layout |

---

##  Tech Stack

- **Backend:** Python 3.x, Django 6
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Database:** SQLite (development)
- **Image Handling:** Pillow
- **Icons:** Bootstrap Icons

---

##  Project Structure

```
RECIPE SHARING/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3              ← created after migrations
│
├── recipeshare/            ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── recipes/                ← Main app (recipes)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── populate_recipes.py
│
├── users/                  ← Auth app
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates/
│   ├── base.html
│   ├── recipes/
│   │   ├── home.html
│   │   ├── recipe_detail.html
│   │   ├── recipe_form.html
│   │   ├── recipe_confirm_delete.html
│   │   └── my_recipes.html
│   └── users/
│       ├── login.html
│       └── register.html
│
├── static/
│   ├── css/style.css
│   └── js/main.js
│
└── media/                  ← Uploaded recipe images (auto-created)
    └── recipe_images/
```

---

## ⚙️ Setup & Installation

### 1. Clone / Download the project

```bash
cd "RECIPE SHARING"
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Load sample data (6 recipes + demo user)

```bash
python manage.py populate_recipes
```

This creates:
- **Demo user:** `chef_demo` / `RecipeShare2024!`
- **6 sample recipes** ready to browse

### 6. (Optional) Create an admin superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

##  Demo Credentials

| Field | Value |
|---|---|
| Username | `chef_demo` |
| Password | `RecipeShare2024!` |
| Admin panel | http://127.0.0.1:8000/admin/ |

---

##  Pages & URLs

| URL | Page |
|---|---|
| `/` | Home — all recipes + search |
| `/recipes/<id>/` | Recipe detail page |
| `/recipes/create/` | Create new recipe (login required) |
| `/recipes/<id>/edit/` | Edit recipe (author only) |
| `/recipes/<id>/delete/` | Delete recipe (author only) |
| `/my-recipes/` | My Recipes dashboard (login required) |
| `/users/register/` | Register new account |
| `/users/login/` | Log in |
| `/users/logout/` | Log out |
| `/admin/` | Django admin panel |

---

##  Security Notes

- CSRF tokens are used on all forms
- Only authenticated users can create recipes
- Only the recipe author can edit or delete their recipe
- Passwords are hashed using Django's built-in auth system
- `DEBUG = True` in development only — change to `False` in production

---

##  Notes

- Recipe images are stored in `/media/recipe_images/`
- The SQLite database (`db.sqlite3`) is created automatically on first migration
- This project is intended for learning/portfolio purposes — for production, switch to PostgreSQL and use environment variables for secrets
