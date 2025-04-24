from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 그리드 초기화 (0~100까지, 2배 확장해서 0~100 사용)
    MAX = 101
    board = [[0]*MAX for _ in range(MAX)]
    
    # 2. 모든 사각형을 2배 확장해서 채움
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2, x2*2+1):
            for y in range(y1*2, y2*2+1):
                board[y][x] = 1
    
    # 3. 각 사각형 내부만 0으로 지워서 테두리만 남김
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2+1, x2*2):
            for y in range(y1*2+1, y2*2):
                board[y][x] = 0
    
    # 4. BFS 초기 설정
    sx, sy = characterX*2, characterY*2
    ex, ey = itemX*2, itemY*2
    q = deque([(sx, sy)])
    dist = [[-1]*MAX for _ in range(MAX)]
    dist[sy][sx] = 0
    
    # 5. 4방향 탐색
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            # 최단거리 // 2 반환어차피
            return dist[y][x] // 2
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAX and 0 <= ny < MAX:
                if board[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((nx, ny))
    return -1  # 도달 불가 시