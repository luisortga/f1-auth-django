# 🏎️ F1 Auth Django

A Django web application for user authentication and Formula 1 driver management.

The project allows users to **register, log in and log out**, and once authenticated, they can create Formula 1 driver records containing a title, driver name, acronym and circuit. The registered drivers are displayed as cards in the application.

This project was developed as a practical exercise to work with **Django authentication, CRUD operations, PostgreSQL, Bootstrap, environment management and deployment**.

## 📸 Preview

![F1 Auth Django Preview](https://i.imgur.com/ICydKup.png)

![F1 Auth Django Drivers](https://i.imgur.com/D6i56vI.png)

## 🚀 Live Demo

The application is deployed on **Render**:

👉 https://f1-auth-django.onrender.com/

## ✨ Features

* 🔐 User registration
* 🔑 Login and logout
* 👤 Authentication-protected driver management
* 🏎️ Create Formula 1 driver records
* 📝 Driver information:

  * Title
  * Name
  * Acronym
  * Circuit
* 🃏 Display drivers as Bootstrap cards
* 🗄️ PostgreSQL database
* 📱 Responsive interface using Bootstrap
* ☁️ Deployment with Render
* 📦 Dependency and virtual environment management with uv

## 🛠️ Technologies

| Technology           | Purpose                                      |
| -------------------- | -------------------------------------------- |
| 🐍 **Python**        | Main programming language                    |
| 🎸 **Django**        | Web framework                                |
| 🐘 **PostgreSQL**    | Relational database                          |
| 🎨 **Bootstrap**     | UI styling and responsive design             |
| ⚡ **uv**             | Python environment and dependency management |
| ☁️ **Render**        | Application deployment                       |
| 🗃️ **Git / GitHub** | Version control                              |

## 📂 Project Structure

```text
f1-auth-django/
│
├── f1django/
│   └── ...
│
├── src/
│   └── f1_rest_api_django/
│       └── ...
│
├── tasks/
│   └── ...
│
├── .gitignore
├── .python-version
├── build.sh
├── LICENSE
├── manage.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## 🔐 Authentication

The application uses Django's built-in authentication system.

Users can:

1. Create an account.
2. Log in.
3. Access the authenticated area.
4. Register Formula 1 drivers.
5. Log out.

Driver creation is restricted to authenticated users.

## 🏎️ Driver Management

After logging in, users can register drivers using the following information:

```text
Title
Name
Acronym
Circuit
```

For example:

```text
Title: Formula 1 Driver
Name: Max Verstappen
Acronym: VER
Circuit: Spa-Francorchamps
```

Once created, the information is stored in PostgreSQL and displayed in the application using Bootstrap cards.

## 🗄️ Database

The application uses **PostgreSQL** as its relational database.

Django's ORM is used to interact with the database, allowing the application to create and retrieve driver records without writing raw SQL for the normal application operations.

## 📦 Environment & Dependencies

This project uses **uv** for Python environment and dependency management.

The project dependencies are defined in `pyproject.toml`, while `uv.lock` contains the resolved versions used by the project.

### Install uv

Follow the official uv installation guide:

https://docs.astral.sh/uv/getting-started/installation/

### Clone the repository

```bash
git clone https://github.com/luisortga/f1-auth-django.git

cd f1-auth-django
```

### Create the environment and install dependencies

```bash
uv sync
```

### Activate the virtual environment

On Windows:

```powershell
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

## ⚙️ Environment Variables

Create a `.env` file in the project root and configure the variables required by the application.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DATABASE_URL=your-postgresql-database-url
```

> Do not commit your `.env` file to GitHub. Sensitive credentials should remain private.

## 🧑‍💻 Running Locally

After installing the dependencies and configuring the environment variables, run the Django development server:

```bash
uv run python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🗃️ Database Migrations

To apply Django migrations:

```bash
uv run python manage.py migrate
```

To create new migrations after modifying models:

```bash
uv run python manage.py makemigrations
```

Then apply them:

```bash
uv run python manage.py migrate
```

## ☁️ Deployment

The application is deployed using **Render**.

The deployment process uses the project's build configuration and the Python dependencies defined through `pyproject.toml` and `uv.lock`.

Production configuration includes:

* PostgreSQL database
* Environment variables
* Django application
* Production build process
* Render web service

## 🎯 Purpose of the Project

This project was created as a practical Django project to explore several concepts involved in building a web application:

* Django project structure
* Django authentication
* CRUD operations
* Forms and model validation
* Django ORM
* PostgreSQL integration
* Bootstrap frontend styling
* Environment variables
* Python dependency management with uv
* Git and GitHub
* Cloud deployment with Render

It also serves as a small Formula 1 themed application where the backend and database concepts can be practiced with a concrete domain.

## 📚 What I Practiced

Through this project I worked with:

```text
Python
   │
   ├── Django
   │    ├── Authentication
   │    ├── Forms
   │    ├── Models
   │    ├── Views
   │    └── Templates
   │
   ├── PostgreSQL
   │
   ├── Bootstrap
   │
   ├── uv
   │
   └── Render
```

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

Made with 🐍 Python, 🎸 Django and 🏎️ Formula 1.
