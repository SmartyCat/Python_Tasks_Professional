import pickle
import sys

data = sys.stdin.readlines()

with open(data[0].rstrip(), "rb") as file:
    func = pickle.load(file)
    args = [d.rstrip() for d in data[1:] if isinstance(d.rstrip(), str)]
    print(func(*args))
