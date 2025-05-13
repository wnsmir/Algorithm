from collections import Counter
    
def solution(clothes):
    sector = []
    k = len(clothes)
    for clothe in clothes:
        sector.append(clothe[1])
    C_sector = Counter(sector)
    
    n = len(C_sector)
    
    answer = 1
    for count in C_sector.values():
        answer *= (count + 1)

    return answer - 1