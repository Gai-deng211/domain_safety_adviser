# Alembic Notes

## What is Alembic?

- Alembic is a **database migration tool** for SQLAlchemy.
- Think of it as **Git for your database schema**—it tracks and manages changes to your database structure over time.
- It allows database updates to be applied in a controlled and versioned manner.

---

## 1. Installation

```bash
pip install alembic
```

---

## 2. Initialize Alembic

```bash
alembic init alembic
```

This creates an `alembic/` directory in your project root.

### Generated files

- `env.py`
- `README.md`
- `script.py.mako`
- `versions/`

---

## 3. Configure `env.py`

Update `env.py` to include:

- Database `Base`
- SQLAlchemy models
- Database URL
- Migration configuration
- Upgrade and downgrade functions

---

## 4. Generate a Migration

```bash
alembic revision --autogenerate -m "describe your changes"
```

Alembic compares your SQLAlchemy models with the current database schema and generates a migration file inside the `versions/` folder.

---

## 5. Apply the Migration

```bash
alembic upgrade head
```

This applies the latest migration to your database.

---

## Typical Workflow

```text
1. Modify your SQLAlchemy models
        ↓
2. Generate a migration
   alembic revision --autogenerate -m "message"
        ↓
3. Review the generated migration
        ↓
4. Apply it
   alembic upgrade head
```