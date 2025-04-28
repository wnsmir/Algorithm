#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
N = 9
M = 9

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

def find_positions(matrix, target):
    positions = []
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if row[j] == target:
                positions.append((i,j))
    return positions

target_cand = []

for row in matrix:
    target_row = max(row)
    target_cand.append(target_row)
target = max(target_cand)

positions = find_positions(matrix, target)
print(target)
for i in positions[0]:
    print(i + 1, end=' ')