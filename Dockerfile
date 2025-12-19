FROM python:3.10-slim

WORKDIR /app

# 1️⃣ Upgrade Python tooling FIRST
RUN pip install --no-cache-dir --upgrade pip wheel setuptools==78.1.1

# 2️⃣ Copy requirements
COPY requirements.txt .

# 3️⃣ Install app dependencies WITHOUT downgrading setuptools
RUN pip install --no-cache-dir --no-deps -r requirements.txt \
 || pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecomm.wsgi:application"]
