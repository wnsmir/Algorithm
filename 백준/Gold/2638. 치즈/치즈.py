from collections import deque

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

turn = 0
last_cheezes = 0

while True:
    # 남은 치즈 개수 세기
    cheezes = sum(grid[i][j] == 1 for i in range(R) for j in range(C))
    if cheezes == 0:
        print(turn)
        break
    last_cheezes = cheezes
    turn += 1

    # 외부 공기만 BFS로 표시
    air = [[False]*C for _ in range(R)]
    queue = deque()
    queue.append((0, 0))
    air[0][0] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 외부공기가 아니면서 일반공기라면
            if 0 <= nx < R and 0 <= ny < C and not air[nx][ny] and grid[nx][ny] == 0:
                air[nx][ny] = True
                queue.append((nx, ny))

    # 3) 외부 공기와 접촉한 치즈 위치 수집
    melt = []
    for x in range(R):
        for y in range(C):
            if grid[x][y] == 1:
                count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if air[nx][ny]:
                        count += 1
                    if count >1:
                        melt.append((x, y))
                        break

    # 4) 치즈 녹이기
    for x, y in melt:
        grid[x][y] = 0