# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies (OpenCV, etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 8080

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Command to run Flask app
CMD ["flask", "run"]
