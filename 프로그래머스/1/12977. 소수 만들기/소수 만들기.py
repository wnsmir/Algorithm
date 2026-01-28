from itertools import combinations

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        num = sum(c)

        if num < 2:
            continue

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            # break 없이 끝난 경우만 실행됨 → 소수
            answer += 1
            
    return answer
            
                
                
    print(candi)