import sys

data = sys.stdin.readlines()
topic = data[-1].strip()
data = list(filter(lambda x: x.split("/")[1].strip() == topic, data[:-1]))
data = list(map(lambda x: x.split("/"), data))
data = sorted(data, key=lambda x: x[0].strip())
data = sorted(data, key=lambda x: int(x[2].strip()))
for d in data:
    print(d[0].strip())
