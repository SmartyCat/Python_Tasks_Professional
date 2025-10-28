def stop_on(iterable, obj):  # первый вариант
    for i in iterable:
        if i == obj:
            break
        yield i


def stop_on(iterable, obj): # второй вариант , больше в одну строку
    iterable = list(iterable)
    return (
        (i for i in iterable[: iterable.index(obj)])
        if obj in iterable
        else (i for i in iterable)
    )


numbers = [1, 2, 3, 4, 5]
print(*stop_on(numbers, 4))
iterator = iter("beegeek")
print(*stop_on(iterator, "a"))
