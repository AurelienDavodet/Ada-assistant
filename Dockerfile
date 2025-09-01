# Use official uv image with Python 3.10
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install system dependencies (compilation etc.)
RUN apt-get update && apt-get install -y gcc build-essential && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    gcc build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency files early to leverage Docker cache
COPY pyproject.toml uv.lock ./

# Create a virtual environment once and sync dependencies
RUN uv venv .venv && \
    uv pip install --upgrade pip && \
    uv sync

# Copy the rest of your application code
COPY . .

# Activate the pre-built venv by default
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Expose Chainlit port
EXPOSE 8000

# Default command
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]
