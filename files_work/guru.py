import sys
from progress import is_arf, is_geom

data = list(map(lambda x: int(x.rstrip()), sys.stdin.readlines()))

if is_arf(data):
    print("Арифметическая прогрессия")
elif is_geom(data):
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")
