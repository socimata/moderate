from functools import cache
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from diskcache import Cache

from .models.endpoint import Endpoint

path = Path(__file__, "../../../data/endpoints").resolve()
if not path.is_dir():
    path.mkdir(parents=True)


@cache
def get_db():
    return Cache[str, Endpoint](path)


def get_endpoint_by_name(name: str):
    return get_db()[name]


def __getattr__(name: Literal["db"]):
    if name == "db":
        return get_db()
    raise AttributeError(f"Module '{__name__}' has no attribute '{name}'")


if TYPE_CHECKING:
    db = get_db()


__all__ = "db", "get_endpoint_by_name"
