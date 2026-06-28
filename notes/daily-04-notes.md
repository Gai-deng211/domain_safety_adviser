# Docker + FastAPI + Alembic + CI/CD Study Notes
# date: June 28, 2026
## 1. Docker Basics

* Docker runs applications inside isolated containers
* Ensures consistency across environments (dev, test, production)
* Installed system-wide (not inside Python venv or project)

### Common Commands

```bash
docker ps              # list running containers
docker run hello-world # test installation
docker compose up -d   # start services in background
docker compose down    # stop services
```

---

## 2. Docker Compose

* Used to run multiple services together (e.g., FastAPI + PostgreSQL)
* Defined using `docker-compose.yml`

### Key Idea

* `docker compose` (new plugin-based system)
* `docker-compose` (legacy standalone tool)

---

## 3. Environment Variables (.env)

### Purpose

* Store secrets and configuration outside code

### Example `.env`

```env
POSTGRES_USER=scrapper
POSTGRES_PASSWORD=scrappermanager
POSTGRES_DB=whoisdb
DATABASE_URL=postgresql+psycopg2://scrapper:scrappermanager@localhost:5432/whoisdb
```

### Important Rule

* Never commit `.env` to GitHub
* Add `.env` to `.gitignore`

---

## 4. Docker Compose Variables

### Usage in `docker-compose.yml`

```yaml
environment:
  POSTGRES_USER: ${POSTGRES_USER}
  POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  POSTGRES_DB: ${POSTGRES_DB}
```

### Key Concept

* Docker Compose automatically loads `.env` from the same directory

---

## 5. PostgreSQL with Docker

### Setup

```yaml
image: postgres:16
ports:
  - "5432:5432"
```

### Result

* DB accessible at:

```
localhost:5432
```

---

## 6. SQLAlchemy + Alembic

### Structure

```
app/database/
    base.py     → Base class
    models.py   → Table definitions
    session.py  → DB connection/session
```

### Alembic Role

* Tracks database schema changes
* Generates migration files automatically

### Commands

```bash
alembic revision --autogenerate -m "init tables"
alembic upgrade head
```

### Critical Rule

* `Base.metadata` must be imported correctly in `alembic/env.py`

---

## 7. FastAPI + Database Dependency

### Pattern

* DB session injected using `Depends(get_db)`

### Common Issue

* Misconfigured DB session causes runtime errors in endpoints like `/health`

---

## 8. CI/CD (GitHub Actions)

### Current Pipeline

* Install Python
* Install dependencies
* Install Playwright
* Run pytest

### Improvement Idea

* Add PostgreSQL service inside CI for full integration testing

---

## 9. System Architecture

```
FastAPI App
    ↓
SQLAlchemy ORM
    ↓
PostgreSQL (Docker)
    ↓
Alembic Migrations
    ↓
GitHub Actions CI
```

---

## 10. Key Takeaways

* Docker = environment consistency
* Docker Compose = multi-service orchestration
* `.env` = secrets/config management
* Alembic = database version control
* FastAPI + SQLAlchemy = backend structure
* CI/CD = automated testing pipeline
