from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    keys = list(ordered_dict.items())
    if not by_values:
        for k in range(len(keys)):
            for i in range(k + 1, len(keys)):
                if keys[k][0] > keys[i][0]:
                    ordered_dict.move_to_end(keys[k][0])
    else:
        for v in range(len(keys)):
            for i in range(v + 1, len(keys)):
                if keys[v][1] > keys[i][1]:
                    ordered_dict.move_to_end(keys[v][0])


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)
data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())
