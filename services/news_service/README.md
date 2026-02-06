# News Generation Service

## Overview

The News Generation Service is a core component of EchoBot, responsible for creating timely and relevant news segments for the broadcast. It uses a sophisticated AI agent to research, write, and produce audio for news articles on various topics.

### Key Features

- **Multi-Source Data Collection**: The service connects to multiple MCP (Multi-Content Protocol) servers to gather information from a wide range of sources, including web search, academic papers, and social media.
- **Topical News Generation**: It is designed to generate news for specific, predefined topics such as "Web3" and "AI & Robotics".
- **End-to-End Content Pipeline**: The service handles the entire news creation process, from data collection and article writing to voice synthesis, saving the final audio files for broadcast.
- **Scheduled Updates**: News generation runs on a schedule to ensure the content remains fresh and up-to-date.

### News Agent

The news agent orchestrates the content creation process. It utilizes a stateful graph to manage the workflow of researching topics, synthesizing information, and generating the final news articles.

![News Agent Graph](src/news_generator_graph.png)

## Configuration

The service is configured through the central `config.py` file and environment variables in `.env`. Key settings include the topics for news generation and the scheduling intervals.

## Getting Started

### Prerequisites

- Docker
- Python 3.12
- An `.env` file in the project root with the necessary environment variables.

### 1. Building the Docker Image

To build the Docker image for the service, run the following command from the project root:

```bash
docker build -t news_service -f services/news_service/Dockerfile .
```

If you need to rebuild the image without using the cache, use the `--no-cache` flag:

```bash
docker build --no-cache -t news_service -f services/news_service/Dockerfile .
```

### 2. Running the Docker Container

Before running, ensure any previous container with the same name is stopped and removed:

```bash
docker stop news_service_container
docker rm news_service_container
```

#### For Development / Debugging

To run the container in the foreground (interactive mode) and see the logs directly in your terminal, use this command. This is recommended for debugging.

**Note:** This command maps the `C:/app/media` directory from your host machine into the container. Ensure this directory exists.

```bash
docker run -it --name news_service_container -v "$(pwd)/logs:/app/logs" -v "//c/app/media:/app/media" --env-file ./.env news_service
```

#### For Production / Detached Mode

To run the container in the background (detached mode), use this command:

```bash
docker run -d --name news_service_container -v "$(pwd)/logs:/app/logs" -v "//c/app/media:/app/media" --env-file ./.env news_service
```

### 3. Managing the Container

#### Checking Logs

If the container is running in detached mode, you can view its logs with this command:

```bash
docker logs -f news_service_container
```

#### Stopping the Container

To stop the running container:

```bash
docker stop news_service_container
```

To remove the stopped container:

```bash
docker rm news_service_container
```

## Running Locally (Without Docker)

For development purposes, you can run the service directly on your machine using a Python virtual environment.

### 1. Create and Activate Virtual Environment

From the project root, create a virtual environment:

```bash
python -m venv venv
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
python -m services.news_service.src.main
```
