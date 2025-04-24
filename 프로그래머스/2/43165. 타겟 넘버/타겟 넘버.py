from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))
    count = 0
    
    while queue:
        index, curr_sum = queue.popleft()
        if index == len(numbers):
            if curr_sum == target:
                count += 1
        else:
            queue.append((index + 1, curr_sum + numbers[index]))
            queue.append((index + 1, curr_sum - numbers[index]))
            
    return count#