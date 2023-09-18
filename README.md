# Django Template

This is a Django template project that I have created for my personal use. It serves as a starting point for Django web
applications and includes several dependencies to help streamline the development process.

I Created this as a part of my django learning journey. So, there may be some poorly written code.

## Dependencies

Here is a list of dependencies used in this project along with their descriptions:

- **Python** (^3.11): The programming language in which Django is built.
- **Django** (^4.2.5): A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **django-environ** (^0.11.2): A library for handling environment variables in Django projects.
- **whitenoise** (^6.5.0): A static file serving library for Django, which simplifies the handling of static files.
- **django-simple-history** (^3.4.0): A Django app that tracks changes to models and allows for easy retrieval of
  historical data.
- **django-crispy-forms** (^2.0): A Django app that helps you control the rendering behavior of Django forms.
- **crispy-tailwind** (^0.5.0): A Django app that integrates the Tailwind CSS framework with crispy-forms to create
  beautiful forms.
- **setuptools** (^68.2.2): A package that helps to manage the distribution and installation of your Python project.

### Development Dependencies

For development purposes, the following dependencies are also included:

- **isort** (^5.12.0): A tool to automatically format and organize Python imports.
- **ruff** (^0.0.290): [Please provide a brief description of what ruff is and how it's used in your project].
- **django-browser-reload** (^1.11.0): [Describe the purpose and usage of django-browser-reload in your project].

## Build Checklist

Before deploying or running your Django project, make sure to perform the following tasks:

- [ ] Run `python manage.py makemigrations` in project root to create database migration files.
- [ ] Run `python manage.py collectstatic` in project root to gather static files for production use.
- [ ] Run `npx tailwindcss -i styles.css -o tailwind.css --build --minify` in `static\src\css` to compile Tailwind CSS
  stylesheets.
- [ ] Run `isort .` in project root to automatically format and organize Python imports.
- [ ] Run `ruff check . --fix` in project root to automatically lint all files.
- [ ] Run `poetry export --format requirements.txt --output requirements/requirements-prod.txt --without-hashes` to
  create requirements file for production.
- [ ] Run `poetry export --format requirements.txt --output requirements/requirements-dev.txt --without-hashes --dev` to
  create requirements file for development.


