from collections import defaultdict

def set_place(grid, turn, students):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n = len(grid)
    friends = students[turn]
    candidates = []

    for x in range(n):
        for y in range(n):
            if grid[x][y] != 0:
                continue
            f_count = 0  # 주변 친구수
            e_count = 0  # 주변 빈칸수

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] in friends:
                        f_count += 1
                    if grid[nx][ny] == 0:
                        e_count += 1

            # 내림차순 정렬을 위해 -f_count, -e_count
            candidates.append((-f_count, -e_count, x, y))

    # 정렬: 친구수 ↓, 빈칸수 ↓, 행 ↑, 열 ↑
    candidates.sort()
    _, _, fx, fy = candidates[0]
    grid[fx][fy] = turn

n = int(input())
students = defaultdict(list)

for _ in range(n*n):
    info = list(map(int, input().split()))
    for i in range(1, 5):
        students[info[0]].append(info[i])
grid = [[0]*n for _ in range(n)]

#순서대로 자리배정
for turn in students:
    set_place(grid, turn, students)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
score = [0, 1, 10, 100, 1000]
satisfied = 0
for x in range(n):
    for y in range(n):
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] in students[grid[x][y]]:
                    count += 1
        satisfied += score[count]

print(satisfied)