from collections import deque

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

fire_q = deque()
jihun_q = deque()
visited = [[False]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jihun_q.append((i, j))
            visited[i][j] = True
        elif maze[i][j] == 'F':
            fire_q.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

time = 0
while jihun_q:
    time += 1

    # 불 확산
    for _ in range(len(fire_q)):
        x, y = fire_q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.' or maze[nx][ny] == 'J':
                    maze[nx][ny] = 'F'
                    fire_q.append((nx, ny))

    # 지훈이 이동
    for _ in range(len(jihun_q)):
        x, y = jihun_q.popleft()
        # 탈출 조건: 가장자리
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            print(time)
            exit()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    jihun_q.append((nx, ny))

print("IMPOSSIBLE")