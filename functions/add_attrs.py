from typing import Any, Callable
from functools import wraps


def add_attrs(**kwargs: Any) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        for k in kwargs:
            func.__dict__[k] = kwargs[k]

        @wraps(func)
        def wrapper(*args: Any, **another_kwargs: Any) -> Any:

            return func(*args, **another_kwargs)

        return wrapper

    return decorator


@add_attrs(attr1="bee", attr2="geek")
def beegeek():
    return "beegeek"


print(beegeek.attr1)
print(beegeek.attr2)


@add_attrs(attr2="geek")
@add_attrs(attr1="bee")
def beegeek():
    return "beegeek"


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
