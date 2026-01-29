FROM python:3.12-slim

LABEL maintainer="SHAdd0WTAka"
LABEL description="Zen AI Pentest Framework"
LABEL version="1.0"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    nmap \
    nikto \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Create non-root user for security
RUN useradd -m -u 1000 pentest && \
    chown -R pentest:pentest /app
USER pentest

# Expose any necessary ports (for future web interface)
EXPOSE 8080

# Default command
CMD ["python", "-m", "zen_ai_pentest", "--help"]
