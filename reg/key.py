from re import sub
import keyword


print(
    sub(
        r"\b(\w+)\b",
        lambda x: (
            "<kw>"
            if x.group(0).lower() in keyword.kwlist
            or x.group(0).capitalize() in keyword.kwlist
            else x.group(0)
        ),
        input()
    )
)
