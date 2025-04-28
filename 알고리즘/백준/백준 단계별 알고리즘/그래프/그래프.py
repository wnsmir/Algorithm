graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} # 무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 # 방향 그래프

def dfs_recursive(graph, node):
    # 방문 결과를 담을 리스트와 방문 여부를 확인할 집합을 만든다.
    res = []
    visited = set()
    
    def _dfs(u):
        if u in visited:
            return
    
        visited.add(u)
        res.append(u)

        for v in graph[u]:
            _dfs(v)
    
    _dfs(node)
    return res

print()