def print_operation_table(operation, rows, cols):
    result = [[operation(i, j) for j in range(1, cols + 1)] for i in range(1, rows + 1)]
    for i in range(rows):
        for j in range(cols):
            print(result[i][j], end=" ")
        print()


print_operation_table(lambda a, b: a * b, 5, 5)

print_operation_table(pow, 5, 4)
