import sys
from datetime import datetime

data = list(
    map(
        lambda x: datetime.strptime(x.rstrip(), "%d.%m.%Y").date(),
        sys.stdin.readlines(),
    )
)
if data == sorted(data):
    print("ASC")
elif data == sorted(data, reverse=True):
    print("DESC")

else:
    print("MIX")
