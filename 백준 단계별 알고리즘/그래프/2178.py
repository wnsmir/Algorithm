from collections import deque
import sys

input = sys.stdin.read
data = input().strip().split('\n')

# 첫 번째 줄에서 N과 M 추출
N, M = map(int, data[0].split())

# 지도 생성
map = []
for i in range(1, N + 1):
    map.append([int(char) for char in data[i]])

start = (0, 0)
end = (N - 1, M - 1)

def bfs_shortest_path(map, start, end, N, M):
    # 네 방향 설정 (오른쪽, 아래, 왼쪽, 위)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 방문 여부와 거리를 저장할 배열 초기화
    visited = [[False] * M for _ in range(N)]
    distance = [[-1] * M for _ in range(N)]
    
    # BFS 시작점 설정
    queue = deque([start])
    visited[start[0]][start[1]] = True
    distance[start[0]][start[1]] = 1  # 시작점 거리 1로 설정
    
    while queue:
        x, y = queue.popleft()
        
        # 목표 지점에 도달한 경우 거리 반환
        if (x, y) == end:
            return distance[x][y]
        
        # 네 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and map[nx][ny] == 1:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    return -1  # 목표 지점에 도달할 수 없는 경우

shortest_distance = bfs_shortest_path(map, start, end, N, M)
print(shortest_distance)