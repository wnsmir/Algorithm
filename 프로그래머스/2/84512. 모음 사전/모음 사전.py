count = 0
answer = 0
found = False

def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U']

    def dfs(path):
        global count, answer, found
        
        if found:
            return
        if path == word:
            answer = count
            found = True
            return
        if len(path) == 5:
            return
        for ch in chars:
            count += 1
            dfs(path + ch)
    
    dfs("")
    return answer