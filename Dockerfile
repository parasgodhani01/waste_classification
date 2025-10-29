# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Create uploads directory
RUN mkdir -p uploads

# Expose the Flask port
EXPOSE 8080

# Set environment variables for Flask
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Run the Flask app
CMD ["python", "app.py"]


# docker build -t parasgodhani/waste-classification-app .
# docker run -p 8080:8080 parasgodhani/waste-classification-app
