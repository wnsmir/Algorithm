def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U']
    count = 0
    answer = 0
    
    def dfs(path):
        nonlocal count, answer
        #답 return
        if word == path:
            answer = count
            return
        #종료조건
        if len(path) == 5:
            return
        for char in chars:
            count += 1
            dfs(path + char)
        
        
    dfs('')
    return answer