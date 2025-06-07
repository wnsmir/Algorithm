from itertools import combinations
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

virus = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 2]
empty_cnt = sum(row.count(0) for row in grid)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 10**9
ans = INF

for case in combinations(virus, M):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    for x, y in case:
        q.append((x, y))
        visited[x][y] = 0

    remain = empty_cnt
    last = 0

    while q and remain:          # 남은 빈칸이 0이면 바로 종료
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1 and grid[nx][ny]!=1:
                visited[nx][ny] = visited[x][y] + 1
                if grid[nx][ny] == 0:      # 새로 감염된 빈칸
                    remain -= 1
                    last = visited[nx][ny] # 최종 시간 후보
                q.append((nx, ny))
                
        if last >= ans:
            break

    if remain == 0:
        ans = min(ans, last)

print(ans if ans != INF else -1)