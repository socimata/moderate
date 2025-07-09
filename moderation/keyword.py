from operator import call

from reactivity.hmr import cache_across_reloads

from keywords import data as keywords


@call
@cache_across_reloads
def keyword_map():
    return {i["keyword"]: i for i in keywords}


def detect_keywords(text: str):
    return [*filter(text.__contains__, keyword_map)]
