def solution(numbers, hand):
    grid = [[0]*3 for _ in range(4)]
    count = 0
    result = ''
    
    # 엄지의 좌표
    thumb  = {}
    thumb['left'] = [3, 0]
    thumb['right'] = [3, 2]
    
    # 키패드 만들기
    for i in range(3):
        for j in range(3):
            count += 1
            grid[i][j] = count
    
    grid[3][0] = '*'
    grid[3][1] = 0
    grid[3][2] = '#'
    
    l_length = 0
    r_length = 0
    
    for num in numbers:
        for i in range(4):
            for j in range(3):
                # grid의 숫자의 좌표 확인
                if num == grid[i][j]:
                    # 좌표가 왼쪽이라면 왼쪽엄지 사용
                    if j == 0:
                        thumb['left'] = [i, j]
                        result += 'L'
                    # 좌표가 오른쪽이라면
                    elif j == 2:
                        thumb['right'] = [i, j]
                        result += 'R'
                    
                    # 좌표가 중간이라면
                    else:
                        # 현재 좌표와 더 가까운 손 찾기
                        left_i, left_j = thumb['left']
                        right_i, right_j = thumb['right'] 
                        
                        l_length = abs(i-left_i) + abs(j-left_j)
                        r_length = abs(i-right_i) + abs(j-right_j)
                        
                        # 왼손이 더 가까우면
                        if l_length < r_length:
                            thumb['left'] = [i, j]
                            result += 'L'
                            
                        #오른손이 더 가까우면
                        elif l_length > r_length:
                            thumb['right'] = [i, j]
                            result += 'R'
                            
                        # 같다면 잡이기준
                        else:
                            thumb[hand] = [i, j]
                            result += hand[0].upper()
                    
            
    return result