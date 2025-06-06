N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 우, 좌, 상, 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 말 위치 및 방향 저장
horses = {}
horse_map = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    horses[i] = [x, y, d]
    horse_map[x][y].append(i)

def rotate(d):
    # 반대 방향: 0 <-> 1, 2 <-> 3
    opposite = [1, 0, 3, 2]
    return opposite[d]

def move(horse_num):
    x, y, d = horses[horse_num]
    nx, ny = x + dx[d], y + dy[d]

    # 현재 칸의 말들
    stack = horse_map[x][y]
    idx = stack.index(horse_num)
    moving = stack[idx:]  # 위에 쌓인 말들
    horse_map[x][y] = stack[:idx]  # 아래 남은 말들

    # 이동할 칸이 벽 또는 파란색이면
    if not (0 <= nx < N and 0 <= ny < N) or grid[nx][ny] == 2:
        d = rotate(d)
        horses[horse_num][2] = d  # 방향 반전 유지
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < N and 0 <= ny < N) or grid[nx][ny] == 2:
            # 이동 불가시 다시 원위치에 말 붙이기
            horse_map[x][y].extend(moving)
            return True

    # 빨간색이면 뒤집기
    if grid[nx][ny] == 1:
        moving.reverse()

    # 이동
    for h in moving:
        horses[h][0], horses[h][1] = nx, ny
        horse_map[nx][ny].append(h)

    # 종료 조건 확인
    if len(horse_map[nx][ny]) >= 4:
        return False
    return True

# 시뮬레이션
for turn in range(1, 1001):
    for i in range(K):
        if not move(i):
            print(turn)
            exit()
print(-1)