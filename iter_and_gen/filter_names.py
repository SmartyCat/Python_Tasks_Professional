from test import digit


def filter_names(names: list, ignore_char: str, max_names: int):
    return (
        item
        for index, item in enumerate(
            (
                name
                for name in names
                if name[0].lower() != ignore_char.lower() and digit(name)
            ),
            start=1,
        )
        if index <= max_names
    )
