from re import sub

print(sub(r"(\b)(\w)(\w)(\w*)(\b)", r"\1\3\2\4\5",input()))
