def solution(d, budget):
    d.sort()
    sum_num = 0
    answer = 0
    for num in d:
        # 예산 넘어가면 이전 값 return
        sum_num += num
        if budget < sum_num:
            return answer
        # 예산이 안넘어가면 다음 수 확인
        else:
            answer += 1
            
    return answer