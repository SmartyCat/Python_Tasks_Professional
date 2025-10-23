from typing import Any, Callable
from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(times):
                try:
                    result = func(*args, **kwargs)
                    if result is not None:
                        return result
                    break
                except:
                    pass
            else:
                raise MaxRetriesException

        return wrapper

    return decorator

@retry(99)
def calculate(a, b, c):
    """Calculate something"""
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

print(calculate.__name__)
print(calculate.__doc__)
try:
    print(calculate(2000, b=1, c=4))
except Exception as e:
    print(type(e))