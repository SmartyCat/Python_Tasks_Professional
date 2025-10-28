from collections import Counter


def unique(iterable):
    if not iterable:
        return None
    return (i for i in Counter(iterable))
