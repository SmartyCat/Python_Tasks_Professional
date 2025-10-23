from functools import wraps


def ignore_exception(*args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args2, **kwargs):
            try:
                func(*args2, **kwargs)
            except Exception as e:
                if any(isinstance(e, i) for i in args):
                    print(f"Исключение {type(e).__name__} обработано")
                else:
                    raise

        return wrapper

    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)


min = ignore_exception(ZeroDivisionError)(min)
try:
    print(min(1, "2", 3, [4, 5]))
except Exception as e:
    print(type(e))
