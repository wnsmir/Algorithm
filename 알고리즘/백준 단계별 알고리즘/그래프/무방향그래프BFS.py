from collections import deque

def bfs_with_order_and_path(graph, start):
    visited = set()  # 방문한 노드를 저장하는 집합
    parent = {node: None for node in graph}
    queue = deque([start])
    visited.add(start)  # 시작 노드를 방문 처리
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)  # 큐에 추가할 때 방문 처리
                parent[neighbor] = node  # 직전 노드 기록
    
    return order, parent

def reconstruct_path(parent, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path if path[0] == start else []

# 예제 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS 탐색 시작
start_node = 'A'
end_node = 'F'
order, parent = bfs_with_order_and_path(graph, start_node)
path = reconstruct_path(parent, start_node, end_node)

print("방문 순서:", order)
print("최단 경로:", path)