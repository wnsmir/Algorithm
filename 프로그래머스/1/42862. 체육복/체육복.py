def solution(n, lost, reserve):
    lost.sort()
    copy_lost = lost[:]
    
    for lo in copy_lost:
        if lo in reserve:
            lost.remove(lo)
            reserve.remove(lo)
    lost.sort()
    copy_lost = lost[:]
    
    for lo in copy_lost:
        #잃어버린 학생 앞에 여벌이 있다면
        if (lo - 1) in reserve:
            lost.remove(lo)
            reserve.remove(lo - 1)
            
        #잃어버린 학생 뒤에 여벌이 있다면
        elif (lo + 1) in reserve:
            lost.remove(lo)
            reserve.remove(lo + 1)
    
    answer = n - len(lost)

    return answer