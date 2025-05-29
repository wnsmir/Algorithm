from collections import deque

def find_fish(grid, baby_shark):
    N = len(grid)
    find = []
    for i in range(N):
        for j in range(N):
            #아기상어보다 작다면 추가
            if 0 < grid[i][j] < baby_shark:
                find.append((i,j))
    return find

#최단거리와 좌표 반환
def bfs(grid, find, start, baby_shark):
    N = len(grid)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[-1]*N for _ in range(N)]
    visited[start[0]][start[1]] = 0
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                #아기상어보다 크면 지나갈 수 없음
                if grid[nx][ny] <= baby_shark:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    answer = None
    min_dist = 987654321

    for f in find:
        fx, fy = f
        dist = visited[fx][fy]
        if dist != -1 and dist < min_dist:
            min_dist = dist
            answer = (fx, fy)
        elif dist == min_dist:
            if fx < answer[0] or (fx == answer[0] and fy < answer[1]):
                answer = (fx, fy)
    
    return min_dist, answer

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            start = (i, j)

baby_shark = 2
total_time = 0
count = 0
while True:
    find = find_fish(grid, baby_shark)
    min_dist, answer = bfs(grid, find, start, baby_shark)

    if answer == None:
        print(total_time)
        break

    else:
        total_time += min_dist
        grid[start[0]][start[1]] = 0
        start = answer
        count += 1
        grid[start[0]][start[1]] = 0
        if count == baby_shark:
            baby_shark += 1
            count = 0