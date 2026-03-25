# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/

# Set working directory to where app.py lives
WORKDIR /app/app

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
