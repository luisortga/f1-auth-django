# 🏎️ F1 Auth Django

A Formula 1 themed web application built with **Python and Django**, featuring user authentication and Formula 1 driver management.

The application allows users to **register, log in and log out**. Once authenticated, users can create Formula 1 driver records containing a title, driver name, acronym and circuit. The registered drivers are displayed as responsive cards.

The project was created as a practical exercise to work with **Django authentication, forms, PostgreSQL, Bootstrap, environment management and cloud deployment**.

## 🔭 Preview

<p align="center">
  <img src="https://i.imgur.com/ICydKup.png" alt="F1 Auth Django" width="850">
</p>

<p align="center">
  <img src="https://i.imgur.com/D6i56vI.png" alt="F1 Auth Django Drivers" width="850">
</p>

## 🐍 Live Demo

The application is deployed on **Render**.

😼 https://f1-auth-django.onrender.com/

## ✨ Features

* 🔐 User registration
* 🔑 Login and logout
* 🛡️ Authentication-protected driver management
* 🏎️ Create Formula 1 driver records
* 📝 Driver information:

  * Title
  * Name
  * Acronym
  * Circuit
* 🧧 Display drivers using responsive Bootstrap cards
* 🗄️ PostgreSQL database
* 📱 Responsive interface
* ☁️ Deployment with Render
* ⚡ Python environment and dependency management with uv

## Technologies

<p align="center">

<a href="https://www.python.org/">
  <img src="https://cdn.simpleicons.org/python" width="55" alt="Python">
</a>
&nbsp;&nbsp;&nbsp;

<a href="https://www.djangoproject.com/">
  <img src="https://cdn.simpleicons.org/django" width="55" alt="Django">
</a>
&nbsp;&nbsp;&nbsp;

<a href="https://www.postgresql.org/">
  <img src="https://cdn.simpleicons.org/postgresql" width="55" alt="PostgreSQL">
</a>
&nbsp;&nbsp;&nbsp;

<a href="https://getbootstrap.com/">
  <img src="https://cdn.simpleicons.org/bootstrap" width="55" alt="Bootstrap">
</a>
&nbsp;&nbsp;&nbsp;

<a href="https://docs.astral.sh/uv/">
  <img src="https://cdn.simpleicons.org/uv" width="55" alt="uv">
</a>
&nbsp;&nbsp;&nbsp;

<a href="https://render.com/">
  <img src="https://cdn.simpleicons.org/render" width="55" alt="Render">
</a>

</p>

| Technology          | Purpose                                      |
| ------------------- | -------------------------------------------- |
| 🐍 **Python**       | Main programming language                    |
| 🎸 **Django**       | Web framework                                |
| 🐘 **PostgreSQL**   | Relational database                          |
| 🎨 **Bootstrap**    | UI styling and responsive design             |
| ⚡ **uv**            | Python environment and dependency management |
| ☁️ **Render**       | Cloud deployment                             |
| 🐙 **Git / GitHub** | Version control                              |

## 🎨 Design & UI

The visual design of the application was developed with a focus on a modern Formula 1 inspired interface.

The backgrounds, translucent elements and **blur / glassmorphism effects** were designed with the assistance of **ChatGPT Codex**, which was used as an AI coding assistant during the development of the frontend.

The interface combines:

* Glassmorphism-inspired cards
* Blurred backgrounds
* Translucent elements
* Responsive Bootstrap components
* Formula 1 inspired visual elements
* Custom CSS styling

> 👾 **AI-assisted development:** ChatGPT Codex was used to assist with the implementation and refinement of the visual design, backgrounds and blur effects.

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

After logging in, users can register drivers using:

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

Once created, the information is stored in PostgreSQL and displayed as a Bootstrap card.

## 🗄️ Database

The application uses **PostgreSQL** as its relational database.

Django's ORM is used to interact with the database and manage Formula 1 driver records.

## 📦 Environment & Dependencies

This project uses **uv** for Python environment and dependency management.

The project's dependencies are defined in `pyproject.toml`, while `uv.lock` contains the resolved dependency versions.

### Clone the repository

```bash
git clone https://github.com/luisortga/f1-auth-django.git

cd f1-auth-django
```

### Install dependencies

```bash
uv sync
```

### Activate the virtual environment

#### Windows

```powershell
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

## ⚙️ Environment Variables

Create a `.env` file in the project root and configure the required environment variables.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-postgresql-database-url
```

> ⚠️ Never commit your `.env` file or expose database credentials and secret keys.

## 🧑‍💻 Running Locally

Apply the database migrations:

```bash
uv run python manage.py migrate
```

Start the development server:

```bash
uv run python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🗃️ Database Migrations

Create migrations after modifying Django models:

```bash
uv run python manage.py makemigrations
```

Apply them:

```bash
uv run python manage.py migrate
```

## ☁️ Deployment

The application is deployed using **Render**.

The production environment uses:

* Django
* PostgreSQL
* Environment variables
* `pyproject.toml`
* `uv.lock`
* Render Web Service

## 🎯 Project Goals

This project was created to practice building a complete Django web application while working with:

* Django project structure
* User authentication
* Forms
* Models
* Views
* Templates
* Django ORM
* PostgreSQL
* Bootstrap
* Custom CSS
* Environment variables
* Python dependency management with uv
* Git and GitHub
* Cloud deployment with Render
* AI-assisted development with ChatGPT Codex

## 🧪 What I Practiced

```text
Python
   │
   └── Django
        ├── Authentication
        ├── Forms
        ├── Models
        ├── Views
        ├── Templates
        └── ORM
             │
             └── PostgreSQL

Frontend
   │
   ├── Bootstrap
   └── Custom CSS
        ├── Glassmorphism
        ├── Blur effects
        └── Responsive design

Development
   │
   ├── uv
   ├── Git
   └── GitHub

Deployment
   │
   └── Render
```

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

Made with 🐍 Python, 🎸 Django and 🏎️ Formula 1.

Design assisted by 🤖 ChatGPT Codex.
