import json
import sys

r = sys.stdin.read()
d = json.loads(r)
for i in d:
    print(
        f"{i}: {", ".join(d[i])}" if type(d[i]).__name__ == "list" else f"{i}: {d[i]}"
    )
