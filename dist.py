def min_distance(d1, d2, d3):
    return min(d1, d2) + min(d1 + d2, d3) + min(max(d1,d2),d3+min(d1,d2))

# Примеры корректных тестов
assert min_distance(1, 2, 3) == 6    # min(1+2+3, 2*1+2*2, 2*1+2*3, 2*2+2*3) = 6
assert min_distance(2, 3, 4) == 9    # min(2+3+4, 4+6, 4+8, 6+8) = 9
assert min_distance(5, 5, 5) == 15   # min(5+5+5, 10+10, 10+10, 10+10) = 15
assert min_distance(1, 1, 10) == 4   # min(1+1+10, 2+2, 2+20, 2+20) = 4