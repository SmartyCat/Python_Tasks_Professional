from typing import Callable, Any
from functools import wraps


def takes(*args: Any) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args2, **kwargs) -> Any:
            if not all(isinstance(a, args) for a in args2) or not all(
                isinstance(kwargs[k], args) for k in kwargs
            ):
                raise TypeError
            return func(*args2, **kwargs)

        return wrapper

    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times


print(repeat_string(string="bee", times=3))


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times


try:
    print(repeat_string("bee", 4))
except TypeError as e:
    print(type(e))
