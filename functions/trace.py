from functools import wraps
from typing import Callable, Any


def trace(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = "'" + result + "'"  # по тестам строки должны быть в кавычках
        print(
            f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}",
            f"TRACE: возвращаемое значение {func.__name__}(): {result}",
            sep="\n",
        )

    return wrapper


@trace
def say(name, line):
    return f"{name}: {line}"


say("Jane", "Hello, World")


@trace
def sub(a, b, c):
    """прекрасная функция"""
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)
