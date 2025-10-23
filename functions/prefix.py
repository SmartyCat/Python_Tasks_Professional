from functools import wraps
from typing import Any, Callable


def prefix(string: str, to_the_end: bool = False) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            return (
                func(*args, **kwargs) + string
                if to_the_end
                else string + func(*args, **kwargs)
            )

        return wrapper

    return decorator


@prefix("€")
def get_bonus():
    return "2000"


print(get_bonus())


@prefix("$$$", to_the_end=True)
def get_bonus():
    return "2000"


print(get_bonus())
