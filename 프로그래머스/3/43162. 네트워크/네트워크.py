from collections import deque

def solution(n, computers):
    network = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                network[i].append(j)
    answer = 0
    queue = deque()
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            queue.append(i)
            while queue:
                curr_node = queue.popleft()
                for neighbor in network[curr_node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
            answer += 1


    return answer