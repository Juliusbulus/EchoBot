FROM ghcr.io/astral-sh/uv:python-3.13-slim AS base

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

FROM base AS dev

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --group dev --group debug

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["tail", "-f", "/dev/null"]

FROM base AS prod

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "services/chat_youtube_service/src/main.py", "--host", "0.0.0.0", "--port", "8000"]