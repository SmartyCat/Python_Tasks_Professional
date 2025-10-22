from typing import Any, Callable


def reverse_args(
    func: Callable[..., Any],
) -> Callable[..., Any]:  # поигрался с аннотацией чтобы набить в этом руку
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args[::-1], **kwargs)

    return wrapper


@reverse_args
def power(a, n):
    return a**n


print(power(2, 3))


@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat("apple", "cherry", "melon"))
