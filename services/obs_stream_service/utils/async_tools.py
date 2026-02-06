import asyncio
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import TypeVar

T = TypeVar("T")


def with_retry(retries: int = 3, delay: float = 2.0):
    """Simple decorator for retrying asynchronous functions."""

    def decorator(func: Callable[..., Coroutine[None, None, T]]):
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            for attempt in range(1, retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception:  # pragma: no cover
                    if attempt == retries:
                        raise
                    await asyncio.sleep(delay)

        return wrapper

    return decorator
