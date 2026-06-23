# WHOIS Domain Intelligence Service

A backend system that scrapes WHOIS data, validates it using Pydantic, stores it in PostgreSQL, caches results with Redis, and exposes a FastAPI REST API for domain intelligence queries.

---

# Tech Stack

* Python
* FastAPI
* Playwright (web scraping)
* PostgreSQL
* Redis (caching)
* SQLAlchemy (ORM)
* Alembic (database migrations)
* Pydantic (data validation)
* Pytest (testing)
* Docker (containerization)

---

# High-Level Architecture

```text id="arch1"
Client
  ↓
FastAPI (API Layer)
  ↓
Service Layer (Business Logic)
  ↓
Redis Cache (fast lookup)
  ↓
Playwright Scraper (WHOIS fetch)
  ↓
Pydantic Validation
  ↓
PostgreSQL (persistent storage)
```

---

# Project Structure

```text id="struct1"
whois-intelligence/

├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── lookup.py
│   │       ├── auth.py
│   │       └── dashboard.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── cache.py
│   │
│   ├── database/
│   │   ├── models.py
│   │   ├── session.py
│   │   └── migrations/   ← Alembic
│   │
│   ├── schemas/
│   │   ├── registration.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── scraper.py
│   │   ├── lookup_service.py
│   │   └── auth_service.py
│   │
│   └── main.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── notes/
│   ├── day01-playwright.md
│   ├── day02-pydantic.md
│   ├── day03-postgres.md
│   ├── day04-fastapi.md
│   ├── day05-redis.md
│   ├── day06-testing.md
│   ├── day07-docker.md
│   └── day08-cicd.md
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt
├── README.md
└── .env
```

---

# Core Features

## Domain Lookup

* Scrape WHOIS data using Playwright
* Normalize raw HTML into structured data
* Validate using Pydantic models

## Caching (Redis)

* Cache recent domain lookups
* Reduce scraping overhead
* Improve response speed

## Persistence (PostgreSQL)

* Store domain lookup history
* Store user accounts
* Track domain metadata over time

## Authentication

* User signup & login
* Password hashing
* JWT-based authentication

## Dashboard

* View past lookups
* Track domain expiration dates
* View cached vs fresh results

---

# API Endpoints

## Public

### Signup

```http id="ep1"
POST /signup
```

### Login

```http id="ep2"
POST /login
```

### Domain Lookup

```http id="ep3"
GET /lookup?domain=example.com
```

---

## Protected

### Dashboard

```http id="ep4"
GET /dashboard
Authorization: Bearer <token>
```

---

# Testing

Run all tests:

```bash id="test1"
pytest
```

Test structure:

* Unit tests → services, parsers
* Integration tests → API endpoints
* DB tests → PostgreSQL interactions

---

# Docker Setup

## Build & run

```bash id="docker1"
docker compose up --build
```

Services:

* FastAPI app
* PostgreSQL
* Redis

---

# Database Migrations (Alembic)

Initialize migrations:

```bash id="alembic1"
alembic init alembic
```

Create migration:

```bash id="alembic2"
alembic revision --autogenerate -m "initial schema"
```

Apply migration:

```bash id="alembic3"
alembic upgrade head
```

---

# Dependencies

Install:

```bash id="req1"
pip install -r requirements.txt
```

Generate file:

```bash id="req2"
pip freeze > requirements.txt
```

---

# Learning Roadmap

## Phase 1 — Scraper (DONE)

* Playwright setup
* WHOIS extraction
* Raw → structured parsing

## Phase 2 — Data Modeling (DONE)

* Pydantic validation
* Data cleaning pipeline

## Phase 3 — Database Layer

* PostgreSQL setup
* SQLAlchemy models
* Alembic migrations

## Phase 4 — API Layer

* FastAPI routes
* Service architecture

## Phase 5 — Caching

* Redis integration
* Cache-first lookup strategy

## Phase 6 — Auth System

* JWT authentication
* User sessions

## Phase 7 — Testing

* Pytest unit tests
* Integration tests

## Phase 8 — Deployment

* Docker setup
* GitHub Actions CI/CD

---

# Final Goal

A production-style backend system that:

* Scrapes real-world WHOIS data
* Validates and normalizes it
* Stores it efficiently
* Serves it via API
* Scales with caching and containers

---

# Future Improvements

* Domain expiry alerts
* Bulk domain scanning
* Domain reputation scoring
* Background job workers (Celery / RQ)
* Rate limiting + API keys
