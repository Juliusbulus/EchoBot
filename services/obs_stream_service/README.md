# OBS Stream Service

## Overview

The OBS Stream Service is the central component for automating the EchoBot broadcast on YouTube. Its primary function is to manage and transition between scenes in OBS Studio according to a predefined schedule, creating a seamless and dynamic live stream.

### Key Features

- **Automated Scene Management**: Connects to OBS Studio via the WebSocket plugin to control scene transitions, media playback, and other stream elements.
- **Schedule-Driven Broadcasting**: Follows a `schedule.json` file to orchestrate the entire broadcast, from intros and music segments to news updates and outros.
- **YouTube Integration**: Designed to work with YouTube Live, managing the stream's lifecycle.

## Setup and Configuration

### 1. OBS Studio Configuration

Before running the service, you need to configure OBS Studio:

- **WebSocket Plugin**: Ensure the OBS WebSocket plugin is installed and enabled. You will need to set a password and provide it in your `.env` file.
- **Scene Collection**: The service uses a predefined scene collection. You can import the provided `EchoBot.json` file into OBS:
    1. In OBS, go to `Scene Collection` > `Import`.
    2. Click `Add` and select the `EchoBot.json` file.
    3. Check the imported collection and click `Import`.
    4. Switch to the newly imported scene collection.

### 2. YouTube Stream Configuration

The YouTube stream is now automatically managed by the YouTube client:

- **Automatic Stream Management**: The system automatically creates and manages YouTube Live streams
- **No Manual Configuration**: No need to manually set `STREAM_ID` in configuration files
- **Dynamic Stream Creation**: When starting the service, it will:
  1. Check for existing active broadcasts
  2. Reuse existing broadcasts if found
  3. Create new broadcasts only when needed

## Getting Started

### Prerequisites

- Docker
- Python 3.12
- OBS Studio with the WebSocket plugin enabled.
- A `.env` file in the project root with the necessary environment variables (including OBS WebSocket credentials).

### 1. Building the Docker Image

To build the Docker image for the service, run the following command from the project root:

```bash
docker build -t obs_stream_service -f services/obs_stream_service/Dockerfile .
```

If you need to rebuild the image without using the cache, use the `--no-cache` flag:

```bash
docker build --no-cache -t obs_stream_service -f services/obs_stream_service/Dockerfile .
```

### 2. Running the Docker Container

Before running, ensure any previous container with the same name is stopped and removed:

```bash
docker stop obs_stream_service_container
docker rm obs_stream_service_container
```

#### For Development / Debugging

To run the container in the foreground (interactive mode) and see the logs directly in your terminal, use this command. This is recommended for debugging.

**Note:** This command maps the `C:/app/media` directory from your host machine into the container. Ensure this directory exists.

```bash
docker run -it --name obs_stream_service_container -p 8001:8000 -v "$(pwd)/logs:/app/logs" -v "//c/app/media:/app/media" --env-file ./.env obs_stream_service
```

#### For Production / Detached Mode

To run the container in the background (detached mode), use this command:

```bash
docker run -d --name obs_stream_service_container -p 8001:8000 -v "$(pwd)/logs:/app/logs" -v "//c/app/media:/app/media" --env-file ./.env obs_stream_service
```

### 3. Managing the Container

#### Checking Logs

If the container is running in detached mode, you can view its logs with this command:

```bash
docker logs -f obs_stream_service_container
```

#### Stopping the Container

To stop the running container:

```bash
docker stop obs_stream_service_container
```

To remove the stopped container:

```bash
docker rm obs_stream_service_container
```

## Running Locally (Without Docker)

For development purposes, you can run the service directly on your machine using a Python virtual environment.

### 1. Create and Activate Virtual Environment

From the project root, create a virtual environment:

```bash
py -m venv .venv
```

Activate the environment:

**Windows:**
```bash
venv\\Scripts\\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

Install the required packages from the `pyproject.toml` file:

```bash
pip install -e .
```

**Note:** The `-e` flag installs the project in "editable" mode, which is useful for development.

### 3. Run the Service

Once the dependencies are installed, you can run the service with the following command:

```bash
python -m services.obs_stream_service.src.main
```
./.venv/Scripts/python -m services.obs_stream_service.src.main