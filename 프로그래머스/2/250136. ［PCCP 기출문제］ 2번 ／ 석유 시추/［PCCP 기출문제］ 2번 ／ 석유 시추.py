def solution(land):
    from collections import deque

    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    col_oil = [0] * m

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                # BFS 시작
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                size = 1
                cols = set()
                cols.add(j)

                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                cols.add(ny)
                                size += 1

                # 걸쳐 있는 열에 석유량 누적
                for c in cols:
                    col_oil[c] += size

    return max(col_oil)