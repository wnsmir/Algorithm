matrix = []
max_length = 0
    
for _ in range(5):
    line = input().strip()
    row = list(line)
    matrix.append(row)
    if len(row) > max_length:
        max_length = len(row)
    
    for row in matrix:
        while len(row) < max_length:
            row.append('')

for i in range(max_length):
    for j in range(5):
        print(matrix[j][i], end="")