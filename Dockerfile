# --- Stage 1: Builder ---
FROM python:3.13-slim AS builder

# Install uv using the official image to avoid needing curl/sh manually
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1
# Use the system python for uv to manage
ENV UV_PYTHON_PREFERENCE=only-system

# Copy only dependency files first to leverage Docker cache
COPY pyproject.toml uv.lock ./

# Sync dependencies into a virtual environment (.venv)
# We use --no-install-project because we haven't copied the source code yet
RUN uv sync --frozen --no-install-project --no-dev


# --- Stage 2: Runtime ---
FROM python:3.13-slim

WORKDIR /app

# Create a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app

# Copy the virtual environment from the builder stage
# This is where the magic happens: we get the libs without the build tools
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv

# Copy the application code
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

# Run the app using the python inside the virtual environment
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]