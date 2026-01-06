def solution(board, moves):
    standby = []
    count = 0
    answer = 0
    
    for y in moves:
        for x in range(len(board)):
            if board[x][y-1] != 0:
                standby.append(board[x][y-1])
                board[x][y-1] = 0
                count += 1
            
                if count > 1 and standby[count-2] == standby[count-1]:
                    standby.pop()
                    standby.pop()
                    answer += 2
                    count -= 2
                
                break

                
    return answer