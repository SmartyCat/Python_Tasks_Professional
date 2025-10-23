from typing import Any, Callable
from functools import wraps


def make_html(tag: str) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            return f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"

        return wrapper

    return decorator


@make_html("del")
def get_text(text):
    return text


print(get_text("Python"))


@make_html("i")
@make_html("del")
def get_text(text):
    return text


print(get_text(text="decorators are so cool!"))
