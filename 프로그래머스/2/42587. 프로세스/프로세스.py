from collections import deque

def check(current, queue):
    for i in range(len(queue)):
        if current[1] < queue[i][1]:
            return False
    return True
    
def solution(priorities, location):
    n = len(priorities)
    loc_pri = []
    
    # 인덱스와 우선순위 튜플쌍으로 저장
    for i in range(n):
        loc_pri.append((i,priorities[i]))
        
    queue = deque()    
    for i in range(n):
        queue.append(loc_pri[i])
    
    answer = []
    
    while queue:
        current = queue.popleft()
        if check(current, queue) == True:
            answer.append(current)
            continue
        else:
            queue.append(current)
            continue
    
    for i in range(n):
        if answer[i][0] == location:
            return i + 1