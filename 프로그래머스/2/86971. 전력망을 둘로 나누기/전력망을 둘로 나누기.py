from collections import defaultdict, deque

def bfs(graph):
    queue = deque()
    visited = set()
    queue.append(1)
    
    while queue:
        curr_node = queue.popleft()
        if curr_node not in visited:
            visited.add(curr_node)
            queue.extend(graph[curr_node])
    
    return len(visited)
            

def solution(n, wires):
    part = 0
    answer = 987654321
    
    for i in range(n):
        i_wires = wires[:i] + wires[i+1:]
        graph = defaultdict(list)
        for a, b in i_wires:
            graph[a].append(b)
            graph[b].append(a)
        
        part = bfs(graph)
        if answer > abs(n - part - part):
            answer = abs(n - part - part)
    
    return answer
        
        
    
    
    
    answer = -1
    return answer