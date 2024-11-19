# Use the official Python image as the base
FROM python:3.10-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that the Django app runs on
EXPOSE 8080

# Default command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
