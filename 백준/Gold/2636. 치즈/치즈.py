from collections import deque

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

turn = 0
last_cheezes = 0

while True:
    # 1) 남은 치즈 개수 세기
    cheezes = sum(grid[i][j] == 1 for i in range(R) for j in range(C))
    if cheezes == 0:
        print(turn)
        print(last_cheezes)
        break
    last_cheezes = cheezes
    turn += 1

    # 2) 외부 공기 BFS 표시 (0,0은 무조건 외부)
    air = [[False]*C for _ in range(R)]
    q = deque([(0,0)])
    air[0][0] = True
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < R and 0 <= ny < C and not air[nx][ny] and grid[nx][ny] == 0:
                air[nx][ny] = True
                q.append((nx,ny))

    # 3) 외부 공기와 닿는 치즈만 녹이기
    melt = set()
    for x in range(R):
        for y in range(C):
            if grid[x][y] == 1:
                for d in range(4):
                    nx,ny = x+dx[d], y+dy[d]
                    if air[nx][ny]:
                        melt.add((x,y))
                        break

    # 4) 치즈 녹이기
    for x,y in melt:
        grid[x][y] = 0