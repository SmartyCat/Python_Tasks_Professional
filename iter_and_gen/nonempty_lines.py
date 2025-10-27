def nonempty_lines(file):
    with open(file, encoding="utf-8") as output_file:
        return (
            i if len(i) <= 25 else "..."
            for i in (line.rstrip() for line in output_file.readlines() if not line.isspace())
        )


print(*nonempty_lines("file"))
