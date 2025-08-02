def solution(cap, n, deliveries, pickups):
    answer = 0
    d = deliveries[:]
    p = pickups[:]
    d_idx = n-1
    p_idx = n-1

    while d_idx >= 0 or p_idx >= 0:
        # 가장 먼 배달/수거 집 찾기
        while d_idx >= 0 and d[d_idx] == 0:
            d_idx -= 1
        while p_idx >= 0 and p[p_idx] == 0:
            p_idx -= 1
        if d_idx < 0 and p_idx < 0:
            break

        # 이번에 가야 할 가장 먼 거리
        far = max(d_idx, p_idx) + 1
        answer += far * 2

        # 한 번에 배달/수거 가능한 cap만큼 뒤에서부터 한 번에 차감
        deliver = cap
        i = d_idx
        while deliver > 0 and i >= 0:
            if d[i] == 0:
                i -= 1
                continue
            if d[i] <= deliver:
                deliver -= d[i]
                d[i] = 0
                i -= 1
            else:
                d[i] -= deliver
                deliver = 0

        pick = cap
        i = p_idx
        while pick > 0 and i >= 0:
            if p[i] == 0:
                i -= 1
                continue
            if p[i] <= pick:
                pick -= p[i]
                p[i] = 0
                i -= 1
            else:
                p[i] -= pick
                pick = 0

    return answer