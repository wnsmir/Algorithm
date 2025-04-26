from collections import deque

def one_letter_diff(word1, word2):
    diff_count = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff_count += 1
    return diff_count

def solution(begin, target, words):
    level = 0
    queue = deque()
    queue.append((begin, 0))
    visited = []
    
    while queue:
        word1, level = queue.popleft()
        if word1 == target:
            return level
        for word2 in words:
            if word2 not in visited:
                if one_letter_diff(word1, word2) == 1:
                    queue.append((word2, level + 1))
                    visited.append(word2)
                
    return 0