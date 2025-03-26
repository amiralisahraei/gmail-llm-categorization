FROM python:3.11-slim

WORKDIR /app

# Install dependencies needed for compilation
RUN apt-get update && apt-get install -y \
    gcc g++ libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY src/ .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

ENV GROQ_API_KEY=""
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
