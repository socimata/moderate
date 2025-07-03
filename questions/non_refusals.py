from operator import call

from reactivity.hmr import cache_across_reloads

from .schema import NonRefusal


@call
@cache_across_reloads
def data() -> list[NonRefusal]:
    from pathlib import Path

    from orjson import loads

    return loads((Path(__file__).parent / "non_refusals.json").read_bytes())
