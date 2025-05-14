from collections import deque

def solution(s):
    character = list(s)
    queue = deque()
    answer = 0
    
    for char in character:
        queue.append(char)
    
    while queue:
        ans = queue.popleft()
        if ans == "(":
            answer += 1
        if ans == ")":
            answer -= 1
        
        if answer < 0:
            return False

    
    if answer == 0:
        return True
    else:
        return False