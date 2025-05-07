def permutations(arr, r):
    result = []
    visited = [False] * len(arr)
    
    def backtrack(path):
        #종료조건
        if len(path) == r:
            result.append(path[:])
            return
        #사용할 수
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                path.append(arr[i])
                backtrack(path)
                path.pop()
                visited[i] = False
    
    backtrack([])
    return result


def solution(k, dungeons):
    r = len(dungeons)
    cases = permutations(dungeons, r)
    max_turn = 0
    for case in cases:
        tired = k
        turn = 0
        for i in range(len(case)):
            if case[i][0] <= tired:
                tired -= case[i][1]
                turn += 1
        if max_turn < turn:
            max_turn = turn

    return max_turn