import json

result = []
with open("/home/kostya/Загрузки/data.json", encoding="utf-8") as input_file, open(
    "updated_data.json", "w", newline="", encoding="utf-8"
) as output_file:
    l = json.load(input_file)
    for i in l:
        if isinstance(i, str):
            result.append(i + "!")
        elif isinstance(i, int) and not isinstance(i, bool):
            result.append(i + 1)
        elif isinstance(i, bool):
            result.append(not i)
        elif isinstance(i, list):
            result.append(i * 2)
        elif isinstance(i, dict):
            i["newkey"] = None
            result.append(i)
    json.dump(result, output_file, ensure_ascii=False)
