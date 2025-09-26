def solution(N, stages):
    
    fail = {}
    count = 0
    for i in range(1, N+1):
        stage_count = 0
        for j in range(len(stages)):
            if stages[j] == i:
                stage_count += 1
        if len(stages) - count == 0:
            fail[i] = 0
        else:
            failure = stage_count/(len(stages) - count)
            fail[i] = failure
            count += stage_count
        
    keys_sorted = [k for k, v in sorted(fail.items(), key=lambda x: x[1], reverse=True)]
        
    return keys_sorted