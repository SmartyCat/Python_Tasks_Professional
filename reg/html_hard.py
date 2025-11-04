from re import findall
import sys

d = {}
for i in sys.stdin.readlines():
    i = i.rstrip()
    tegs = findall(r"<(\w+)", i)
    attr = findall(r'([\w-]+)="', i)
    for t in tegs:
        for a in attr:
            cur = i[i.index("<" + t) :]
            if a in cur[1 : cur.index(">")]:
                d.setdefault(t, set()).add(a)
        else:
            if t not in d:
                d[t] = set()
else:
    for i in sorted(d.items(), key=lambda x: x[0]):
        print(f"{i[0]}: {", ".join(sorted(i[1]))}")
