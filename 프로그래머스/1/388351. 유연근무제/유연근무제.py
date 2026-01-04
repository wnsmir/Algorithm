def solution(schedules, timelogs, startday):
    answer = 0
    
    auth_time = []
    for sc in schedules:
        hour = sc // 100
        minute = sc % 100 + 10
        
        # 한시간을 넘기면
        if minute >= 60:
            minute -= 60
            hour += 1
            
        auth_time.append((hour, minute))
    
    # 각 사원별 반복
    i = 0
    for timelog in timelogs:
        # 제한 시간, 제한 분
        check = 0 # check가 7이 되면 상품 get
        
        limit_hour = auth_time[i][0]
        limit_min = auth_time[i][1]
        i += 1
        today = startday -1
        # 한 사원의 타임라인과 리밋 비교
        for time in timelog:
            today += 1
            if today > 7:
                today %= 7
                
            # 오늘이 주말이면 check +1 하고 continue
            if today == 6 or today == 7:
                check += 1
                continue
                
            cur_hour = time // 100
            cur_min = time % 100
            
            # 출근시간이 제한시간보다 느리면 탈락
            if cur_hour > limit_hour:
                check = 0
                continue
            # 분 지각했을때
            elif cur_hour == limit_hour:
                if cur_min > limit_min:
                    check = 0
                    continue
            # 다 통과하면 check += 1
            check += 1
        
        if check == 7:
            answer += 1

    return answer