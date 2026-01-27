from collections import defaultdict

def solution(N, stages):
    failure = defaultdict(float)

    # 현재 사람 수
    now = len(stages)
    # 각 스테이지 반복
    for i in range(N):
        # 각 반복마다 count 초기화
        count = 0
        for num in stages:
            # 각 스테이지에 있는 사람 수 count
            if (i+1) == num:
                count += 1
        failure[i+1] = 0.0 if now == 0 else count / now
        now -= count
        print(count, now)
    
    sorted_items = sorted(failure.items(), key=lambda kv: (-kv[1], kv[0]))
    
    answer = [stage for stage, rate in sorted_items]

    return answer
        