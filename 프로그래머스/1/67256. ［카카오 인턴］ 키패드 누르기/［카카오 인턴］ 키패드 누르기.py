def solution(numbers, hand):
    result = ''
    
    # 키패드
    pad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]
    
    # 오른손 왼손
    left = (3, 0)
    right = (3, 2)
    cur_x, cur_y = 0, 0
    
    for i in range(len(numbers)):
        # 현재 숫자 위치
        for x in range(4):
            for y in range(3):
                if pad[x][y] == numbers[i]:
                    cur_x, cur_y = x, y
                    
        if numbers[i] in [1, 4, 7]:
            left = (cur_x, cur_y)
            result += 'L'
            continue

        if numbers[i] in [3, 6, 9]:
            right = (cur_x, cur_y)
            result += 'R'
            continue
        
        # 현재 손과의 거리비교
        # 오른손과의 거리비교
        right_distance = abs(right[0] - cur_x) + abs(right[1] - cur_y)
        left_distance = abs(left[0] - cur_x) + abs(left[1] - cur_y)
        
        if right_distance > left_distance:
            left = (cur_x, cur_y)
            result += 'L'
        
        elif right_distance < left_distance:
            right = (cur_x, cur_y)
            result += 'R'
        
        # 오른손 왼손 거리가 같다면
        else: 
            if hand == "right":
                right = (cur_x, cur_y)
                result += 'R'    
            else:
                left = (cur_x, cur_y)
                result += 'L'
        
    return result