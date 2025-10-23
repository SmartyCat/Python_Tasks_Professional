from typing import Any, Callable
from functools import wraps


def square(
    func: Callable[..., Any],
) -> int | float:  # простой декоратор, решил поэксперементировать с аннтоациямми
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> int | float:
        return func(*args, **kwargs) ** 2

    return wrapper


@square
def add(a, b):
    """прекрасная функция"""
    return a + b


print(add(1, 1))
print(add.__name__)
print(add.__doc__)
