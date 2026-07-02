# Docker + FastAPI + PostgreSQL (Summary Notes)
# Date: July 1, 2026
## 1. Dockerfile vs Docker Compose

### Dockerfile
- Builds a single application image
- Defines:
  - base image (python:3.12)
  - dependencies
  - app code
  - startup command (CMD)

### docker-compose.yml
- Runs multiple containers together
- Example: FastAPI + PostgreSQL
- Handles networking, ports, environment, dependencies

---

## 2. Key Difference

- Dockerfile → builds image
- Compose → runs containers

---

## 3. FastAPI Container Basics

### Service name
```yaml
api: