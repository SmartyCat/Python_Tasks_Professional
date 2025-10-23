from typing import Callable, Any
from functools import wraps


def returns_string(func: Callable[..., Any]) -> str | TypeError:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str | TypeError:
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result
        raise TypeError

    return wrapper


@returns_string
def beegeek():
    return "beegeek"


print(beegeek())


@returns_string
def add(a, b):
    return a + b


try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))
