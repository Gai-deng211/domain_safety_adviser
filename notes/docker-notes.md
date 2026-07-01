# 🐳 Docker Notes
_Date: June 30, 2026_

---

## Docker Compose: `docker-compose.yml`

Docker Compose lets you define, configure, and run **multiple containers** from a single configuration file.

### Main Sections

- **`version:`** Specifies the Compose file version (e.g., `"3.9"`).
- **`services:`** List of containers (services) to run.
    - **`image:`** The Docker image to use for this service.
    - **`container_name:`** Sets a custom name for your container.
    - **`restart:`** Policy for automatic restarts (e.g., `always`).
    - **`env_file:`** Loads environment variables from a `.env` file.
    - **`environment:`** Passes additional environment variables to the container.
    - **`ports:`** Maps host:container ports (format: `host_port:container_port`).
    - **`volumes:`** Mounts persistent volumes inside the container.

#### Example: PostgreSQL Data Volume

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```
- Ensures database data persists beyond container lifecycle.

---

## Dockerfile

A **Dockerfile** is a step-by-step recipe for building a Docker image.

### Typical Structure

```dockerfile
FROM python:3.12              # Start from an official Python base image
WORKDIR /app                  # Set the working directory inside the image
COPY requirements.txt .       # Add requirements file
RUN pip install --no-cache-dir -r requirements.txt   # Install dependencies
COPY . .                      # Copy the entire application code to the image
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  # Start FastAPI app
```

---

## Useful Docker Compose Commands

```bash
docker compose up -d      # Launch containers in detached mode
docker compose down       # Stop and remove containers and networks
docker compose ps         # List running containers
docker compose logs       # Show aggregated logs from services
docker compose build      # Build (or rebuild) images
```

---

## Summary

- **Dockerfile**: Defines how your app image is built.
- **Docker Compose**: Orchestrates running one or more containers together.
- **`.env` file**: Store configuration and secrets outside of code.
- **Volumes**: Use for persistent storage (e.g., database data).
- **Port mapping**: Expose container services to your host.
- **Containers** are stateless, but **volumes** keep data safe across runs.