def parse_ranges(ranges: str):
    ranges = ranges.split(",")
    return (
        j
        for i in (r.split("-") for r in ranges)
        for j in range(int(i[0]), int(i[1]) + 1)
    )


print(*parse_ranges("7-32"))
