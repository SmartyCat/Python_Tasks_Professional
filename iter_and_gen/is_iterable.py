from typing import Any


def is_iterable(obj: Any) -> bool:
    try:
        obj = iter(obj)
        return True
    except TypeError:
        return False


objects = [(1, 13), 7.0004, [1, 2, 3]]
for obj in objects:
    print(is_iterable(obj))
