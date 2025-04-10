from collections import deque

INF = 987654321
# 동, 서, 남, 북 이동 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = ['동', '서', '남', '북']

def find_exit(grid, N):
    """
    원래 grid (N×N)에서 값이 3인 위치 주변에 0이 있으면,
    그 방향에 따라 확장 grid(2*M×8*M) 상의 출구 좌표를 계산하여 반환.
    (출구 좌표는 문제 조건에 맞게 오프셋을 조정)
    """
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 3:
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 0:
                        direction = directions[d]
                        if direction in ['남', '북']:
                            position = j   # 열 기준
                        else:
                            position = i   # 행 기준
                        if direction == '동':
                            exit1_x, exit1_y = 2 * M - 1, position
                            exit2_x, exit2_y = 2 * M - 1, position + M * 4
                        elif direction == '남':
                            exit1_x, exit1_y = 2 * M - 1, position + M
                            exit2_x, exit2_y = 2 * M - 1, position + M * 5
                        elif direction == '서':
                            exit1_x, exit1_y = 2 * M - 1, position + M * 2
                            exit2_x, exit2_y = 2 * M - 1, position + M * 6
                        elif direction == '북':
                            exit1_x, exit1_y = 2 * M - 1, position + M * 3
                            exit2_x, exit2_y = 2 * M - 1, position + M * 7
                        return exit1_x, exit1_y, exit2_x, exit2_y
    return None, None, None, None

def rotate_matrix(matrix, angle):
    """행렬을 시계 방향으로 angle(°) 만큼 회전"""
    if angle == 90:
        return [list(row) for row in zip(*matrix[::-1])]
    elif angle == 180:
        return [row[::-1] for row in matrix[::-1]]
    elif angle == 270:
        return [list(row) for row in zip(*matrix)][::-1]
    else:
        return matrix

def bfs(current_x, current_y, exit1_x, exit1_y, exit2_x, exit2_y, grid):
    """
    확장 grid (2*M×8*M)에서 BFS로 시작점에서 출구까지의 최소 거리를 계산.
    """
    queue = deque()
    queue.append((current_x, current_y))
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    distance = [[INF]*cols for _ in range(rows)]
    visited[current_x][current_y] = True
    distance[current_x][current_y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    d1 = distance[exit1_x][exit1_y]
    d2 = distance[exit2_x][exit2_y]
    return -1 if d1 == INF and d2 == INF else min(d1, d2)

def strange_bfs_with_obstacle(start_x, start_y, target_x, target_y, grid, strange, min_score):
    """
    시간의 벽 통과 후, 실제 미지의 공간에서 BFS를 수행하면서,
    각 BFS 턴마다 실제 턴 = min_score + BFS 이동 횟수에 따라 장애물(이상좌표)을 확산.
    장애물은 strange 리스트에 [r, c, direction_index, v] 형식으로 주어지며,
    각 장애물은 v턴마다 한 칸씩 주어진 방향으로 이동하고, 해당 칸을 벽(1)으로 만듭니다.
    """
    N_grid = len(grid)
    visited = [[False]*N_grid for _ in range(N_grid)]
    distance = [[0]*N_grid for _ in range(N_grid)]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    distance[start_x][start_y] = 0

    while q:
        x, y = q.popleft()
        current_turn = distance[x][y]
        actual_turn = min_score + current_turn  # 실제 턴

        # 장애물 확산 처리
        for obs in strange:
            v = obs[3]
            if actual_turn % v == 0:
                sx, sy, d_index = obs[0], obs[1], obs[2]
                nx = sx + dx[d_index]
                ny = sy + dy[d_index]
                if 0 <= nx < N_grid and 0 <= ny < N_grid and grid[nx][ny] != 1:
                    grid[nx][ny] = 1
                    obs[0] = nx
                    obs[1] = ny

        if x == target_x and y == target_y:
            return current_turn

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N_grid and 0 <= ny < N_grid and grid[nx][ny] != 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = current_turn + 1
                    q.append((nx, ny))
    if distance[target_x][target_y] == INF:
        return -1
    else:
        return distance[target_x][target_y]

def build_extended_grid(time_top):
    """
    time_top: M×M 행렬 (남쪽 데이터)
    
    남쪽 블록: 원본 time_top  
    동쪽 블록: time_top을 270° 회전  
    북쪽 블록: time_top을 180° 회전  
    서쪽 블록: time_top을 90° 회전  

    이 네 개의 블록을 남, 동, 북, 서 순서로 이어붙이고,
    그 순서를 다시 반복하여 가로로 8개의 M×M 블록을 만들고,
    이를 두 번 쌓아 2*M × 8*M 크기의 확장 grid를 구성합니다.
    """
    M = len(time_top)
    block_south = time_top                        
    block_east  = rotate_matrix(time_top, 270)
    block_north = rotate_matrix(time_top, 180)
    block_west  = rotate_matrix(time_top, 90)

    row_blocks = []
    for i in range(M):
        row = (block_south[i] + block_east[i] +
               block_north[i] + block_west[i] +
               block_south[i] + block_east[i] +
               block_north[i] + block_west[i])
        row_blocks.append(row)
    extended_grid = row_blocks + row_blocks
    return extended_grid

# ─────────────────────────────────────────────────────────
# 메인 실행 부분

# 입력 처리
N, M, F = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
time_east  = [list(map(int, input().split())) for _ in range(M)]
time_west  = [list(map(int, input().split())) for _ in range(M)]
time_south = [list(map(int, input().split())) for _ in range(M)]
time_north = [list(map(int, input().split())) for _ in range(M)]
time_top   = [list(map(int, input().split())) for _ in range(M)]
strange    = [list(map(int, input().split())) for _ in range(F)]

# 장애물 초기 배치: 장애물의 시작 위치를 grid에 1로 설정
for obs in strange:
    r, c, d_index, v = obs
    if 0 <= r < N and 0 <= c < N:
        grid[r][c] = 1

exit1_x, exit1_y, exit2_x, exit2_y = find_exit(grid, N)
score = []

# 서쪽 붙이기 (time_top을 90° 회전)
time_west_top = rotate_matrix(time_top, 90)
west_grid = []
for i in range(M):
    west_grid.append([0]*(2*M) + time_west_top[i] + [0]*(5*M))
for i in range(M):
    west_grid.append(time_east[i] + time_south[i] + time_west[i] + time_north[i] +
                     time_east[i] + time_south[i] + time_west[i] + time_north[i])
score.append(bfs(0, 0, exit1_x, exit1_y, exit2_x, exit2_y, west_grid))

# 북쪽 붙이기 (time_top을 180° 회전)
time_north_top = rotate_matrix(time_top, 180)
north_grid = []
for i in range(M):
    north_grid.append([0]*(3*M) + time_north_top[i] + [0]*(4*M))
for i in range(M):
    north_grid.append(time_east[i] + time_south[i] + time_west[i] + time_north[i] +
                      time_east[i] + time_south[i] + time_west[i] + time_north[i])
score.append(bfs(0, 0, exit1_x, exit1_y, exit2_x, exit2_y, north_grid))

# 동쪽 붙이기 (time_top을 270° 회전)
time_east_top = rotate_matrix(time_top, 270)
east_grid = []
for i in range(M):
    east_grid.append([0]*(4*M) + time_east_top[i] + [0]*(3*M))
for i in range(M):
    east_grid.append(time_east[i] + time_south[i] + time_west[i] + time_north[i] +
                     time_east[i] + time_south[i] + time_west[i] + time_north[i])
score.append(bfs(0, 0, exit1_x, exit1_y, exit2_x, exit2_y, east_grid))

# 남쪽 붙이기 (time_top 그대로 사용)
south_grid = []
for i in range(M):
    south_grid.append([0]*(5*M) + time_top[i] + [0]*(2*M))
for i in range(M):
    south_grid.append(time_east[i] + time_south[i] + time_west[i] + time_north[i] +
                      time_east[i] + time_south[i] + time_west[i] + time_north[i])
score.append(bfs(0, 0, exit1_x, exit1_y, exit2_x, exit2_y, south_grid))

min_score = min(score)

# 미지의 공간 장애물 확산 처리 및 BFS 수행
# 출발지점: grid에서 값이 3인 곳의 인접한 0 (첫 발견)
for i in range(N):
    for j in range(N):
        if grid[i][j] == 3:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 0:
                    start_x, start_y = ni, nj

# 탈출지점: grid에서 값이 4인 곳 (첫 발견)
for i in range(N):
    for j in range(N):
        if grid[i][j] == 4:
            target_x, target_y = i, j

min_distance = strange_bfs_with_obstacle(start_x, start_y, target_x, target_y, grid, strange, min_score)

if min_score == -1 or min_distance == -1:
    print(-1)
else:
    print(min_score + min_distance)