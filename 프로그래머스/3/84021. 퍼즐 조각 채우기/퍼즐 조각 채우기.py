from collections import deque

def bfs(board, target):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    N = len(board)
    visited = [[False]*N for _ in range(N)]
    shapes = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == target and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                shape = [(i, j)]  # i, j를 기준으로 좌표 저장

                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] == target and not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                                shape.append((nx, ny))
                shapes.append(shape)
    return shapes

def normalize(shape):
    INF = 987654321
    min_x = INF
    min_y = INF
    for coordinate in shape:
        if coordinate[0] < min_x:
            min_x = coordinate[0]
        if coordinate[1] < min_y:
            min_y = coordinate[1]
    
    normalized = []
    for coordinate in shape:
        x = coordinate[0] - min_x
        y = coordinate[1] - min_y
        normalized.append((x, y))
                          
    return sorted(normalized)

def rotate(shape):
    return [(y, -x) for x, y in shape]                          
    
def solution(game_board, table):
    answer = 0
    blanks = bfs(game_board, 0)
    puzzles = bfs(table, 1)
    
    for puzzle in puzzles:
        matched = False
        for blank in blanks:
            if len(puzzle) != len(blank):
                continue
            for _ in range(4):
                puzzle = rotate(puzzle)
                if normalize(puzzle) == normalize(blank):
                    answer += len(puzzle)
                    matched = True
                    blanks.remove(blank)
                    break
            if matched:
                break
    
    return answer