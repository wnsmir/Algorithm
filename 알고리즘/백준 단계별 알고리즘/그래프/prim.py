import heapq

def prim(vertices, edges):
    mst = []
    visited = set()
    adj = {v: [] for v in vertices}
    
    for u, v, weight in edges:
        adj[u].append((weight, v))
        adj[v].append((weight, u))
    
    # 시작 정점을 'A'로 설정 (임의의 정점으로 시작 가능)
    start_vertex = vertices[0]
    min_heap = [(0, start_vertex)]  # (가중치, 정점)
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        
        if weight != 0:
            mst.append((u, weight))
        
        for edge in adj[u]:
            next_weight, v = edge
            if v not in visited:
                heapq.heappush(min_heap, (next_weight, v))
    
    return mst

# 예제 사용법
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 6),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 9),
    ('D', 'F', 7),
    ('E', 'F', 5)
]

mst = prim(vertices, edges)
print("MST:", mst)