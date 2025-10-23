# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies for OpenCV and others
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 8080

# Set environment variable (for Flask or FastAPI)
ENV PORT=8080

# Command to run the app
# Uncomment the line that matches your framework

# If you're using Flask (e.g., app.py)
# CMD ["python", "app.py"]

# If you're using FastAPI (e.g., main.py)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
