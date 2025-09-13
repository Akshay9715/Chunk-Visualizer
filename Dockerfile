# Dockerfile
FROM python:3.11-slim

# working dir
WORKDIR /app

# small system deps (safe default for building some wheels)
RUN apt-get update && apt-get install -y build-essential --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# copy only requirements first to use Docker cache
COPY requirements.txt .

# ensure pip is recent and install dependencies
RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# copy the rest of the project
COPY . .

# default port (container listens on this)
ENV PORT=5000
EXPOSE 5000

# Serve with gunicorn (Flask app object is `app` in main.py)
ENTRYPOINT sh -c "gunicorn -w 4 -b 0.0.0.0:${PORT} main:app"
