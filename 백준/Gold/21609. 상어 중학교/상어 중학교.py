from collections import deque

def bfs(grid):
    N = len(grid)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    max_blocks = []
    max_rainbow = 0

    for x in range(N):
        for y in range(N):
            # (x, y)부터 새로 시작하는 BFS에서는 반드시 visited도 새로 초기화
            color = None
            blocks = []
            rainbow = 0

            # 시작 칸이 일반 블록(>0)이 아니면 건너뛰기
            if grid[x][y] <= 0:
                continue

            queue = deque()
            queue.append((x, y))
            blocks.append((x, y))
            visited[x][y] = 1

            while queue:
                cx, cy = queue.popleft()
                if grid[cx][cy] != 0 and grid[cx][cy] != -1:
                    color = grid[cx][cy]

                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                        # 무지개 블록
                        if grid[nx][ny] == 0:
                            queue.append((nx, ny))
                            blocks.append((nx, ny))
                            rainbow += 1
                            visited[nx][ny] = 2
                        # 일반 블록이면서 색이 같은 경우
                        elif grid[nx][ny] != -1 and color is not None and grid[nx][ny] == color:
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                            blocks.append((nx, ny))

            # 무지개 블록만 다시 미방문으로
            for i in range(N):
                for j in range(N):
                    if visited[i][j] == 2:
                        visited[i][j] = -1

            # 그룹 최소 조건 검사
            if color is None or len(blocks) < 2:
                continue

            # 그룹 우선순위 비교: 크기 → 무지개 수 → 기준 블록
            if len(max_blocks) < len(blocks):
                max_blocks = blocks[:]
                max_rainbow = rainbow

            elif len(max_blocks) == len(blocks):
                if rainbow > max_rainbow:
                    max_blocks = blocks[:]
                    max_rainbow = rainbow

                elif rainbow == max_rainbow:
                    max_std = (N, N)
                    for bx, by in max_blocks:
                        if grid[bx][by] > 0:
                            if (bx < max_std[0]) or (bx == max_std[0] and by < max_std[1]):
                                max_std = (bx, by)

                    cur_std = (N, N)
                    for bx, by in blocks:
                        if grid[bx][by] > 0:
                            if (bx < cur_std[0]) or (bx == cur_std[0] and by < cur_std[1]):
                                cur_std = (bx, by)

                    if (cur_std[0] > max_std[0]) or (cur_std[0] == max_std[0] and cur_std[1] > max_std[1]):
                        max_blocks = blocks[:]
                        max_rainbow = rainbow

    # 가능한 그룹을 다 찾은 뒤
    if not max_blocks:
        return False

    score = len(max_blocks) * len(max_blocks)
    for bx, by in max_blocks:
        grid[bx][by] = -2
    return score

def gravity(grid):
    N = len(grid)
    for x in range(N-2, -1, -1):
        for y in range(N):
            if grid[x][y] < 0:
                continue
            nx = x
            while nx + 1 < N and grid[nx + 1][y] == -2:
                grid[nx+1][y], grid[nx][y] = grid[nx][y], -2
                nx += 1

def rotate(grid):
    N = len(grid)
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[N-j-1][i] = grid[i][j]
    for i in range(N):
        for j in range(N):
            grid[i][j] = new_grid[i][j]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
total_score = 0

while True:
    visited = [[-1]*N for _ in range(N)]
    score = bfs(grid)
    if score is False:
        print(total_score)
        break

    total_score += score
    gravity(grid)
    rotate(grid)
    gravity(grid)