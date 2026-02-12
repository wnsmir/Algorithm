# 최소 피로도는 넘겨야 하며
# 소모 피로도 소모됨
# 던전은 하루에 하나씩 탐험가능
# 던전 탐험은 하루에 한번씩 
from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)
    max_count = 0
    
    # 던전 수 만큼 반복
    arr = []
    for i in range(N):
        arr.append(i)
    
    permu_list = list(permutations(arr))
    
    for i in range(len(list(permu_list))):
        count = 0
        case = permu_list[i]
        now = k
        for c in case:
            # 현재 피로도보다 임계피로도가 더 작으면 가능
            if now >= dungeons[c][0]:
                # 소모 피로도만큼 제거
                now -= dungeons[c][1]
                
                count += 1
            # 임계 피로도가 더 높으면 이번 반복문은 건너뛰기
            else:
                break
        
        # 최대치 변경
        if max_count <= count:
            max_count = count
        
    return max_count
                
                
                