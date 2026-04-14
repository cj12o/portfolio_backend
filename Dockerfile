FROM python:3.13-slim

WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*


# Create non-root user FIRST
RUN useradd -m appuser

# Give ownership of /app BEFORE switching user
RUN chown -R appuser:appuser /app

#switch 
USER appuser

# Set PATH for this user
ENV PATH="/home/appuser/.local/bin:$PATH"

# Install uv as appuser
RUN curl -Ls https://astral.sh/uv/install.sh | sh

# Copy dependency files
COPY --chown=appuser:appuser pyproject.toml uv.lock ./


#Install dependencies
RUN uv sync --frozen

# Copy app code
COPY --chown=appuser:appuser . .

EXPOSE 8000

CMD ["uv","run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

