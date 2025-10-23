from typing import Callable, Any
from functools import wraps


def repeat(times: int) -> Callable[..., Any]:
    def decorater(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:
            for i in range(times):
                result = func(*args, **kwargs)
            if result is not None:
                return result

        return wrapper

    return decorater


@repeat(3)
def say_beegeek():
    """documentation"""
    print("beegeek")


say_beegeek()


@repeat(10)
def add(a, b):
    """sum of two numbers"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))
