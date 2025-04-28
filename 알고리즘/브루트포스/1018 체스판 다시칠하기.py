import sys

input = sys.stdin.read
data = input().splitlines()

# 행과 열의 개수 읽기
rows, cols = map(int, data[0].split())
grid = []

# 그리드 데이터 저장
for i in range(1, rows + 1):
    row = list(data[i])
    grid.append(row)

# 8x8 블록을 검사하기 위한 범위 계산
y_matrix = rows - 7
x_matrix = cols - 7

def count_changes(start_row, start_col):
    # 두 가지 패턴을 정의
    pattern1 = ['B', 'W']
    pattern2 = ['W', 'B']
    
    changes1 = 0
    changes2 = 0

    for i in range(8):
        for j in range(8):
            expected1 = pattern1[(i + j) % 2]
            expected2 = pattern2[(i + j) % 2]
            
            if grid[start_row + i][start_col + j] != expected1:
                changes1 += 1
            if grid[start_row + i][start_col + j] != expected2:
                changes2 += 1

    return min(changes1, changes2)

# 각 8x8 블록을 검사하여 최소 교체 수 계산
min_changes = float('inf')

for j in range(y_matrix):
    for i in range(x_matrix):
        min_changes = min(min_changes, count_changes(j, i))

print(min_changes)