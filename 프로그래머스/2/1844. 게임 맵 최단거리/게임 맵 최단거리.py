from collections import deque

def solution(maps):
    INF = 987654321
    dx = [0, 0, 1, -1]  # x: 좌우
    dy = [1, -1, 0, 0]  # y: 상하
    
    N = len(maps)      # 세로 길이 (행)
    M = len(maps[0])   # 가로 길이 (열)
    
    queue = deque()
    queue.append((0, 0))
    
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    distance = [[INF] * M for _ in range(N)]
    distance[0][0] = 1

    while queue:
        x, y = queue.popleft()
        
        if x == M - 1 and y == N - 1:
            return distance[y][x]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    queue.append((nx, ny))
                    
    return -1