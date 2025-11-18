import heapq
T = int(input())
INF = 987654321
tc = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(T):
    N = int(input())
    dist = [[INF]*N for _ in range(N)]
    tc += 1
    heap = []
    grid = [list(map(int, input().split())) for _ in range(N)]
    heapq.heappush(heap, (grid[0][0], 0, 0))
    dist[0][0] = grid[0][0]

    while heap:
        cost, x, y = heapq.heappop(heap)
        if cost > dist[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + grid[nx][ny]
                if new_cost < dist[nx][ny]:
                    heapq.heappush(heap, (new_cost, nx, ny))
                    dist[nx][ny] = new_cost
    
    print(f"#{tc} {dist[N-1][N-1]}")