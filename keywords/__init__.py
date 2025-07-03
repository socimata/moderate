from operator import call

from reactivity.hmr import cache_across_reloads

from .schema import Keyword


@call
@cache_across_reloads
def data() -> list[Keyword]:
    from pathlib import Path

    from orjson import loads

    return loads((Path(__file__).parent / "data.json").read_bytes())


__all__ = ["data"]
