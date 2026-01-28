matrix = [
    [0, 0, 5],
    [0, 0, 0],
    [8, 0, 0]
]

sparse = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            sparse.append((i, j, matrix[i][j]))

print("Sparse Matrix (row, column, value):")
for item in sparse:
    print(item)
