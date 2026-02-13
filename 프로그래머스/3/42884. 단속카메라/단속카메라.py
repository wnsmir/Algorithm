def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    
    while routes:
        # 카메라를 마지막 위치에 고정
        camera = routes[0][1]
        answer += 1
        for i in range(len(routes)-1, -1, -1):
            # 카메라가 커버되는 구간 삭제
            if routes[i][0] <= camera <= routes[i][1]:
                routes.pop(i)
    
    return answer