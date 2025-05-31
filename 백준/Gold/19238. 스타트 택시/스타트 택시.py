from collections import deque

N, M, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
start = (x-1, y-1)

# 출발 좌표: [도착x, 도착y]
users = dict()
for _ in range(M):
    sx, sy, dx, dy = map(int, input().split())
    users[(sx-1, sy-1)] = [dx-1, dy-1]

def bfs(grid, start, destination):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append(start)
    visited = [[-1]*N for _ in range(N)]
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 1:
                if visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[destination[0]][destination[1]]

def find_dest(grid, start, users):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append(start)
    visited = [[-1]*N for _ in range(N)]
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 1:
                if visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    # 손님 후보 (거리, 행, 열)로 저장
    target = []
    for (sx, sy) in users:
        dist = visited[sx][sy]
        if dist != -1:
            target.append((dist, sx, sy))
    if not target:
        return (-1, -1), -1, (-1, -1)  # 손님 없음

    target.sort()
    _, sx, sy = target[0]
    dx, dy = users[(sx, sy)]
    destination = (dx, dy)
    spend_to_user = visited[sx][sy]
    return destination, spend_to_user, (sx, sy)

for _ in range(M):
    destination, spend_to_user, user_pos = find_dest(grid, start, users)
    if spend_to_user == -1 or fuel < spend_to_user:
        print(-1)
        exit()
    # 택시가 손님에게 감
    fuel -= spend_to_user
    # 손님을 태우고 목적지로 감
    spend_to_destination = bfs(grid, user_pos, destination)
    if spend_to_destination == -1 or fuel < spend_to_destination:
        print(-1)
        exit()
    fuel -= spend_to_destination
    fuel += spend_to_destination * 2
    start = destination
    del users[user_pos]

print(fuel)