def solution(name):
    n = len(name)
    
    #알파벳조절을 위한 이동횟수
    char_count = 0
    for char in name:
        char_count += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    #커서 이동 횟수
    min_move = 987654321
    for i in range(n):
        next = i + 1
        A_count = 0
        while next < n and name[next] == 'A':
            next += 1
            A_count += 1
        move1 = i *2 + (n -next)
        move2 = (n -next) *2 + i
        min_move = min(min_move, move1, move2)
    
    answer = char_count + min_move
    
    return answer