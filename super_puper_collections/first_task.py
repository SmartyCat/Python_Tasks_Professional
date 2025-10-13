from collections import namedtuple
import pickle

with open("/home/kostya/Загрузки/data.pkl", "rb") as file:
    Animal = namedtuple("Animal", ["name", "family", "sex", "color"])
    data = pickle.load(file)
    for d in data:
        name, family, sex, color = d._fields
        print(
            f"{name}: {d.name}\n{family}: {d.family}\n{sex}: {d.sex}\n{color}: {d.color}\n"
        )
