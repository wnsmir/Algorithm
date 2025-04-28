def dfs_topological_sort(vertices, edges):
    def dfs(node):
        nonlocal visited, stack, adj_list
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    # 인접 리스트 초기화
    adj_list = {i: [] for i in range(vertices)}
    for src, dest in edges:
        adj_list[src].append(dest)

    visited = [False] * vertices
    stack = []

    # 모든 노드에 대해 DFS 수행
    for v in range(vertices):
        if not visited[v]:
            dfs(v)
    
    # 스택에 쌓인 노드를 역순으로 반환하여 위상 정렬 결과를 얻음
    return stack[::-1]

# 예제 사용법
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(dfs_topological_sort(vertices, edges))