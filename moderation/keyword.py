from operator import call

from reactivity.hmr import cache_across_reloads

from keywords import data as keywords


@call
@cache_across_reloads
def keyword_map():
    return {i["keyword"]: i for i in keywords}


def detect_keywords(text: str, deduplicate=True):
    results = [*filter(text.__contains__, keyword_map)]

    if deduplicate:
        for i, keyword in enumerate(reversed(s := sorted(results, reverse=True, key=len)), start=1):
            for other in s[:-i]:
                if keyword in other:
                    results.remove(keyword)
                    break

    return results
