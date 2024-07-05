def dfs_stack_with_parent(graph, start):
    visited = set()
    stack = [start]
    parent = {start: None}  # 시작 노드의 부모는 None
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent[neighbor] = node  # 직전 노드 기록

    return order, parent

def reconstruct_path(parent, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent.get(node, None)
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

# DFS 탐색 시작
order, parent = dfs_stack_with_parent(graph, 'A')
path = reconstruct_path(parent, 'A', 'F')

print("방문 순서:", order)
print("경로 복원:", path)