def solution(lottos, win_nums):
    result = []
    
    lo_count = 0
    count = 0
    for lo in lottos:
        if lo == 0:
            lo_count += 1
        else:
            # 로또 번호를 맞추면
            if lo in win_nums:
                count += 1
    
    def check(num):
        if num == 6:
            return 1
        elif num == 5:
            return 2
        elif num == 4:
            return 3
        elif num == 3:
            return 4
        elif num ==2:
            return 5
        else:
            return 6

    result.append(check(lo_count + count))
    result.append(check(count))
    
    return result