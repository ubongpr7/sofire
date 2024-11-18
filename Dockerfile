# Use Alpine-based Python image
FROM python:3.12-alpine

# Set environment variables for Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    build-base \
    jpeg-dev \
    zlib-dev \
    postgresql-dev

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Set the default command to run the app
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
