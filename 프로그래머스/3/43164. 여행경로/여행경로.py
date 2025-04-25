from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    route = []
    
    def dfs(airport):
        while graph[airport]:
            next = graph[airport].pop()
            dfs(next)
        route.append(airport)
    
    dfs("ICN")
    
    return route[::-1]