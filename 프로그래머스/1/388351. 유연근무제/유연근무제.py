def solution(schedules, timelogs, startday):
    answer = 0
    limit_time = []
    # 인덱스별로 시간제한 추가
    for time in schedules:
        temp = str(time)
        r_time = temp.split(":")
        limit_time.append(r_time)

    idx = 0
    for times in timelogs:
        flag = True
        day = startday
        for t in times:
            # 주말이면 pass
            if day == 6 or day == 7:
                day += 1
                continue
            else:
                # 주말이 지나면 1로 초기화
                if day == 8:
                    day = 1
                
                # 출근시간안에 들어오면
                limit = str(int(limit_time[idx][0]) + 10)
                if len(limit) == 3:
                    if int(limit[1]) >= 6:
                        temp = list(limit)
                        temp[0] = str(int(temp[0]) + 1)
                        temp[1] = str(int(temp[1]) - 6)
                        temp = ''.join(temp)
                        limit = int(temp)
                    else:
                        limit = int(limit_time[idx][0]) + 10
                        
                elif len(limit) == 4:
                    if int(limit[2]) >= 6:
                        temp = list(limit)
                        temp[1] = str(int(temp[1]) + 1)
                        temp[2] = str(int(temp[2]) - 6)
                        temp = ''.join(temp)
                        limit = int(temp)
                    else:
                        limit = int(limit_time[idx][0]) + 10

            
                if limit >= t:
                    day += 1
                    continue
                # 지각하면 탈락
                else:
                    flag = False
                    break
                        
        # 7일모두 통과하면
        if flag == True:
            answer += 1
        # 다음사람
        idx += 1
        
    return answer