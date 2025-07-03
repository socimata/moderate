from operator import call

from reactivity.hmr import cache_across_reloads

from .schema import Generation


@call
@cache_across_reloads
def data() -> list[Generation]:
    from pathlib import Path

    from orjson import loads

    return loads((Path(__file__).parent / "generations.json").read_bytes())
