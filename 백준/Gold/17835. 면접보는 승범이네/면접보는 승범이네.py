N, M, K = map(int, input().split())

import heapq
def dijkstra(spots, graph, N):
    INF = 10**18
    dist = [INF] * (N+1)
    heap = []

    for start in spots:
        dist[start] = 0
        heapq.heappush(heap, (0, start))
    
    while heap:
        d, cur = heapq.heappop(heap)
        if dist[cur] < d:
            continue
        # WTG == Where To Go
        for WTG, cost in graph[cur]:
            if dist[WTG] > d + cost:
                dist[WTG] = d + cost
                heapq.heappush(heap, (dist[WTG], WTG))
    
    return dist


graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, c = map(int, input().split())
    graph[v].append((u, c))

spots = list(map(int, input().split()))

farest_dist = -1
city = 0
dist = dijkstra(spots, graph, N)

for i in range(1, N+1):
    if dist[i] > farest_dist:
        farest_dist = dist[i]
        city = i
    if dist[i] == farest_dist and i < city:
        city = i

print(city)
print(farest_dist)