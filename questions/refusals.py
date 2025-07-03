from operator import call

from reactivity.hmr import cache_across_reloads

from .schema import Refusal


@call
@cache_across_reloads
def data() -> list[Refusal]:
    from pathlib import Path

    from orjson import loads

    return loads((Path(__file__).parent / "refusals.json").read_bytes())
