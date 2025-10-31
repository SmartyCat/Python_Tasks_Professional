s = input()

for i in range(len(s)):
    result = s[i : i + 15].split("-")
    if s[i] == "7" and "".join(s[i : i + 15].replace("-", "")).isdigit():
        if (
            len(result[1]) == 3
            and len(result[2]) == 3
            and len(result[3]) == 2
            and len(result[4]) == 2
        ):
            print("-".join(result))
    elif s[i] == "8" and "".join(s[i : i + 15].replace("-", "")).isdigit():
        if len(result[1]) == 3 and len(result[2]) == 4 and len(result[3]) == 4:
            print("-".join(result))
