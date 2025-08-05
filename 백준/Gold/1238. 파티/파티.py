import heapq

def dijkstra(N, graph, X):
    INF = 10**18
    dists = [INF] * (N+1)
    heap = []

    dists[X] = 0
    heapq.heappush(heap, (0, X))

    while heap:
        dist, cur = heapq.heappop(heap)
        if dists[cur] < dist:
            continue
        for end, cost in graph[cur]:
            if dists[end] > dist + cost:
                dists[end] = dist + cost
                heapq.heappush(heap, (dists[end], end))
    
    return dists

N, M, X = map(int, input().split())

graph_1 = [[] for _ in range(N+1)]
graph_2 = [[] for _ in range(N+1)]

for i in range(M):
    start, end, cost = map(int, input().split())
    graph_1[start].append((end, cost))
    graph_2[end].append((start, cost))

# X에서 집으로 돌아가는 거리
dists_1 = dijkstra(N, graph_1, X)
dists_2 = dijkstra(N, graph_2, X)

dists = [0] * (N+1)
max_cost = 0
for i in range(1, N+1):
    dists[i] = dists_1[i] + dists_2[i]
    if max_cost < dists[i]:
        max_cost = dists[i]

print(max_cost)