from collections import deque

def bfs_shortest_path(graph, start):
    visited = set()
    queue = deque([start])
    dist = {start : 0}
    prev = {start : None}

    visited.add(start)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                prev[neighbor] = node
                dist[neighbor] = dist[node] + 1
    return dist, prev

def reconstruct_path(end, prev):
    path = []
    at = end

    while at is not None:
        path.append(at)
        at = prev[at]
    
    path.reverse()
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'
distance, previous_nodes = bfs_shortest_path(graph, start_node)
path = reconstruct_path(end_node, previous_nodes)
print(path)
print(distance)