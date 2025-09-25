def solution(board, moves):
    stack = []
    N = len(board)
    
    for move in moves:
        j = move - 1
        for i in range(N):
            # 인형이 없으면 pass
            if board[i][j] == 0:
                continue
            else:
                stack.append(board[i][j])
                board[i][j] = 0
                break
    
    prev_stack = len(stack)
    flag = True
    while flag == True:
        flag = False
        prev = ''
        for i in range(len(stack)):
            if prev == stack[i]:
                del stack[i]
                del stack[i-1]
                flag = True
                break
            else:
                prev = stack[i]            
    
    
    answer = prev_stack - len(stack)
    return answer