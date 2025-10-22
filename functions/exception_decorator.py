from typing import Any, Callable


def exception_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            value = func(*args, **kwargs)
            return (value, "Функция выполнилась без ошибок")
        except Exception:
            return (None, "При вызове функции произошла ошибка")

    return wrapper


@exception_decorator
def f(x):
    return x**2 + 2 * x + 1


print(f(7))

sum = exception_decorator(sum)
print(sum(["199", "1", 187]))
