FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS base

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg git tmux && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Builder stage
FROM base AS dev

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --group dev --group debug

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["tail", "-f", "/dev/null"]

# Production stage
FROM base AS prod

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "start_services.py"]