def solution(progresses, speeds):
    answer = []
        
    while len(progresses) > 0:
        # 하루마다 각자의 스피트만큼 진전
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                progresses[i] = 100
            else:
                progresses[i] += speeds[i]
            
        count = 0       
        for i in range(len(progresses)):
            if progresses[0] == 100:
                count += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        if count != 0:
            answer.append(count)
        
    return answer