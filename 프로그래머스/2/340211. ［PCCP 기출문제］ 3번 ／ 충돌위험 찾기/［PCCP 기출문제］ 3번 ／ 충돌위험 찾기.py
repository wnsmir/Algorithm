def solution(points, routes):
    # 1) 포인트 번호 → 좌표 매핑
    point_coords = {i+1: tuple(coord) for i, coord in enumerate(points)}
    
    # 2) 로봇 초기화: pos = 시작 좌표, idx = routes[0] → routes[1] 로 가기 위한 인덱스
    robots = []
    for route in routes:
        robots.append({
            'route': route,
            'pos': point_coords[route[0]],
            'idx': 1
        })
    
    risk = 0  # 위험 상황 누적 카운트
    
    # 3) 시뮬레이션: 로봇이 한 명도 남지 않을 때까지 반복
    while robots:
        # --- (A) 현재 시간 t에서 충돌 체크 ---
        cnt = {}
        for r in robots:
            cnt[r['pos']] = cnt.get(r['pos'], 0) + 1
        for v in cnt.values():
            if v >= 2:
                risk += 1

        # 새로운 로봇 리스트를 만들기 위한 빈 리스트
        remaining_robots = []

        # 모든 로봇을 돌면서
        for r in robots:
            # 아직 목적지가 남아 있는 로봇만 추가
            if r['idx'] < len(r['route']):
                remaining_robots.append(r)

        # robots 리스트를 갱신
        robots = remaining_robots

        # 로봇이 모두 도착해서 남은 게 없으면 루프 종료
        if len(robots) == 0:
            break
        
        # --- (C) 나머지 로봇을 1초 동안 한 칸씩 이동시키기 ---
        for r in robots:
            target = point_coords[r['route'][r['idx']]]
            cr, cc = r['pos']
            tr, tc = target
            
            # r 좌표 우선 이동
            if cr != tr:
                cr += 1 if tr > cr else -1
            else:
                cc += 1 if tc > cc else -1
            
            r['pos'] = (cr, cc)
            
            # 이동 후 도착했으면 다음 세그먼트로
            if (cr, cc) == target:
                r['idx'] += 1
    
    return risk