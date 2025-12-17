# Base image with Python
FROM python:3.11-slim

# Environment variables for predictable Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY main.py /app/main.py

# Expose port used by the application
EXPOSE 8000

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
