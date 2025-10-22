from typing import Callable, Any


def takes_positive(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not all(isinstance(a, int) for a in args) or not all(
            isinstance(kwargs[k], int) for k in kwargs
        ):
            raise TypeError
        elif not all(a > 0 for a in args) or not all(kwargs[k] > 0 for k in kwargs):
            raise ValueError
        return func(*args, **kwargs)

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum("10", 20, 10))
except Exception as err:
    print(type(err))
