# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables for performance
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100

# Create a working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# create a new directory to save output
RUN mkdir ./output

# Install other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY src/ ./src

# Config
ARG GROQ_API_KEY
ENV PYTHONUNBUFFERED=1

# Set default command
CMD ["python", "src/app.py"]
