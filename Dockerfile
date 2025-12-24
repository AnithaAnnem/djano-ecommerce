FROM python:3.10-slim

WORKDIR /app

# -----------------------------
# Environment
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ecomm.settings

# -----------------------------
# System deps
# -----------------------------
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Python tooling
# -----------------------------
RUN pip install --no-cache-dir --upgrade pip wheel setuptools==78.1.1

# -----------------------------
# Install deps
# -----------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy project
# -----------------------------
COPY . .

# -----------------------------
# 🔥 FIX: IGNORE .map FILES 🔥
# -----------------------------
RUN python manage.py collectstatic --noinput --ignore "*.map"

# -----------------------------
# Runtime
# -----------------------------
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecomm.wsgi:application"]
