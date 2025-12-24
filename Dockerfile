FROM python:3.10-slim

WORKDIR /app

# -----------------------------
# Environment variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ecomm.settings
ENV DJANGO_COLLECTSTATIC=1

# -----------------------------
# System dependencies (minimal)
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Python tooling
# -----------------------------
RUN pip install --no-cache-dir --upgrade pip wheel setuptools==78.1.1

# -----------------------------
# Install dependencies
# -----------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy project
# -----------------------------
COPY . .

# -----------------------------
# Collect static safely
# -----------------------------
RUN python manage.py collectstatic --noinput

# -----------------------------
# Runtime
# -----------------------------
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecomm.wsgi:application"]
