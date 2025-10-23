from typing import Any, Callable
from functools import wraps


def strip_range(start: int, end: int, char: str = ".") -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)
            return result[:start] + len(result[start:end]) * char + result[end:]

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(3, 20, "_")
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(20, 30)
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(1, 2, "-")
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(100, 200, "=")
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(0, 300, "=")
def beegeek():
    return "beegeek"


print(beegeek())


@strip_range(0, 4, "=")
def beegeek():
    return "beegeek"


print(beegeek())



@strip_range(0, 1)
def beegeek(word, end=" "):
    """This is... Requiem. What you are seeing is indeed the truth"""
    return word + end

print(beegeek("beegee", end="k"))
print(beegeek.__name__)
print(beegeek.__doc__)