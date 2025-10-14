from collections import defaultdict


def flip_dict(dict_of_lists):
    result = defaultdict(list)
    for i in dict_of_lists:
        for j in dict_of_lists[i]:
            result[j].append(i)
    return result


data = {
    "Arthur": ["cacao", "tea", "juice"],
    "Timur": ["coffee", "tea", "juice"],
    "Anri": ["juice", "coffee"],
}
for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
