from typing import Any


def is_iterator(obj: Any) -> bool:
    return obj == iter(obj)
