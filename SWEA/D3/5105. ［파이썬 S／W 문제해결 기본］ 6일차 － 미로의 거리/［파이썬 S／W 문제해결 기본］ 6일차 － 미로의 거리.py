from collections import deque

T = int(input())
tc = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start, grid):
    x, y = start
    queue = deque()
    dist = [[-1]*N for _ in range(N)]
    dist[x][y] = 0
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        # 도착지면 해당거리 출력
        if grid[x][y] == 3:
            return int(dist[x][y])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            # 방문 안하고 통로면
            if dist[nx][ny] == -1 and grid[nx][ny] != 1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return 0

for _ in range(T):
    tc += 1
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    # 시작, 끝 지점 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                start = (i, j)
            if grid[i][j] == 3:
                end = (i, j)

    answer = bfs(start, grid)
    if answer != 0:
        answer -= 1

    print(f"#{tc} {answer}")