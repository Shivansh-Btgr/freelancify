FROM python:3.13.4-slim

WORKDIR /app

# Install system dependencies including PostgreSQL client libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE $PORT

# Start with migrations and runserver
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT"]