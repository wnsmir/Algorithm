from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    #각 코스메뉴 구성수마다 모든주문에서 가능한 조합 추출
    for c_len in course:
        combs = []
        for order in orders:
            combs += combinations(sorted(order), c_len)
            
        comb_counter = Counter(combs)
        if len(comb_counter) == 0:
            continue
        else:
            max_count = max(comb_counter.values())
            for comb, cnt in comb_counter.items():
                if cnt == max_count and cnt > 1:
                    answer.append(''.join(comb))
                
    return sorted(answer)