<div align="center">

# TattooAI Studio

**From an idea to a sketch, and from a sketch to your artist.**

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?style=flat-square&logo=django&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini_API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)

[Getting started](#getting-started) • [Environment variables](#environment-variables)

</div>

---

## Team

- **Daria Burenko**
- **Antonii Polovko**


## About the project

TattooAI Studio is a web application for a tattoo studio that helps clients find their artist and visualize the idea of their future tattoo. The main goal is to simplify communication between the client and the tattoo artist at the sketch development stage with the help of artificial intelligence.

### What makes the project special

> *"I don't know how to explain it"*

Integration with a generative AI API (Gemini API) to create an approximate tattoo sketch from the client's text description. This solves the problem above and gives the artist a visual basis for understanding the client's idea before developing the final custom design.

### Main features

- **Catalog:** artists with filtering by style and viewing of their work.
- **Accounts:** registration, authentication, and profile management.
- **Requests:** creating a tattoo session request with attached references and generated sketches.
- **Artist account:** personal account for the artist with a history of client requests.

### Roles

| Role | What they can do |
| --- | --- |
| **Guest** | Browse the catalog of artists, their portfolios, available styles, and general information about the studio |
| **User (Client)** | Generate draft sketches with the AI tool, save them in their profile, and send a request to a chosen artist for refinement and to book a session |
| **Tattoo artist** | Access a request panel with the AI sketches and idea descriptions sent by clients, and manage their own portfolio |
| **Administrator** | Manage the list of artists, styles, bookings, and platform content |

---

## Getting started

**You will need:** Python 3.12 or newer and Git.

### 1. Clone the repository

```bash
git clone https://github.com/da-renok/tattooAI.git
cd tattooAI
```

### 2. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the `.env` file

```bash
cp .env.example .env
```

Then fill it in as described in [Environment variables](#environment-variables). At minimum, replace `DJANGO_SECRET_KEY`.

### 5. Run the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/>

---

## Environment variables

| Variable | Required | Description |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Yes | Django secret key, individual for each developer |
| `DEBUG` | No (default `True`) | `True` for local development, `False` in production |
| `ALLOWED_HOSTS` | No (default `localhost,127.0.0.1`) | Comma-separated hosts the server answers to |
| `GEMINI_API_KEY` | Not yet | Gemini API key for the upcoming sketch generation feature |

### Django secret key

Everyone generates their own key for local development. With the virtual environment activated, run:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output into `.env`:

```env
DJANGO_SECRET_KEY='your-generated-key'
```

### Gemini API key

The key is required for AI sketch generation. There are two ways to get one:

- **Ask the team** for our shared key. We share it privately.
- **Generate your own** in [Google AI Studio](https://aistudio.google.com/api-keys): sign in with a Google account, click **Create API key**, and copy it.

Add it to `.env`:

```env
GEMINI_API_KEY='your-gemini-api-key'
```