FROM python:3.12-slim

# Install ffmpeg for audio processing
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only the pyproject.toml to leverage Docker layer caching
COPY services/obs_stream_service/pyproject.toml ./

# Install dependencies from pyproject.toml
RUN pip install --no-cache-dir .

# Copy the rest of the application code
COPY . .

# Set PYTHONPATH to make imports work correctly from the root
ENV PYTHONPATH=/app

# Create and set permissions for media directories in a single layer
RUN mkdir -p /app/media/{news,voice,music,state,memory,videos,config} && \
    chmod -R 755 /app/media/

CMD ["python", "services/obs_stream_service/src/main.py"]