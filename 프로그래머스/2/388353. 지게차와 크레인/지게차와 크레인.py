from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0]) if n > 0 else 0

    # 패딩 포함한 grid 생성 (실제 내용은 [1..n][1..m])
    grid = [[0] * (m + 2)]
    for row in storage:
        grid.append([0] + list(row) + [0])
    grid.append([0] * (m + 2))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs():
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visited[nx][ny]:
                    if grid[nx][ny] in (0, 1):
                        visited[nx][ny] = True
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                        q.append((nx, ny))

    for request in requests:
        selected = []
        if len(request) == 2:  # 크레인: 첫 문자 기준으로 해당 물건들을 '비운 자리(1)'로 표시하고 외부 확장
            target = request[0]
            for x in range(1, n + 1):
                for y in range(1, m + 1):
                    if grid[x][y] == target:
                        selected.append((x, y))
            for x, y in selected:
                grid[x][y] = 1
            bfs()
        elif len(request) == 1:  # 지게차: 외부(0)와 인접한 target만 제거
            target = request
            bfs()  # 최신 외부 상태 반영
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if grid[i][j] == target:
                        for d in range(4):
                            ni = i + dx[d]
                            nj = j + dy[d]
                            if grid[ni][nj] == 0:
                                selected.append((i, j))
                                break
            for x, y in selected:
                grid[x][y] = 0

    # 남은 실제 물건(0,1 아닌 것) 개수 세기
    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] not in (0, 1):
                count += 1
    return count