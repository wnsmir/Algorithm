from collections import deque

N, T = map(int, input().split())
taste = [[[c] for c in input()] for _ in range(N)]
trust = [list(map(int, input().split())) for _ in range(N)]

#T번째 하루 시작
for i in range(T):
    #아침이 되면 모든 학생은 신앙심 +1
    for j in range(N):
        for k in range(N):
            trust[j][k] += 1

    #점심: 그룹 발견 -> 대표 선정 -> 신앙심 전달 계획 (반복)
    gods = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False]*N for _ in range(N)]
    trust_updates = [[0] * N for _ in range(N)] # 신앙심 변화를 임시 저장

    for j in range(N):
        for k in range(N):
            if not visited[j][k]:
                # 1. 새로운 그룹 발견 및 그룹원 탐색
                group_members = []
                q = deque([(j, k)])
                visited[j][k] = True
                group_members.append((j, k))
                current_taste_set = set(taste[j][k])

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N and \
                           not visited[nx][ny] and \
                           set(taste[nx][ny]) == current_taste_set:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            group_members.append((nx,ny))
                
                # 2. 발견된 그룹 내에서 대표자 선정
                leader_pos = group_members[0]
                for (r, c) in group_members:
                    if trust[r][c] > trust[leader_pos[0]][leader_pos[1]]:
                        leader_pos = (r, c)
                    elif trust[r][c] == trust[leader_pos[0]][leader_pos[1]]:
                        leader_pos = min(leader_pos, (r, c))

                gods.append([leader_pos, trust[leader_pos[0]][leader_pos[1]]])
                
                # 3. 대표에게 신앙심 전달 계획 (원래 로직: +/- 1)
                for (r, c) in group_members:
                    if (r, c) != leader_pos:
                        trust_updates[r][c] -= 1
                        trust_updates[leader_pos[0]][leader_pos[1]] += 1
    
    # 4. 모든 신앙심 변화를 일괄 적용
    for r in range(N):
        for c in range(N):
            trust[r][c] += trust_updates[r][c]

    # 5. 저녁 전파를 위해 god list의 신앙심 정보 업데이트
    for god in gods:
        leader_pos = god[0]
        god[1] = trust[leader_pos[0]][leader_pos[1]]


    #저녁시간 신앙을 전파
    propagations = []
    for god in gods:
        xx, yy = god[0]
        dd = trust[xx][yy] # 업데이트된 신앙심 사용
        kind = len(taste[xx][yy])
        propagations.append([kind, -dd, xx, yy])
    propagations.sort()
    
    # 이번 턴에 전파당한 학생(대표) 목록
    propagated_to_this_turn = set()

    #방향 지정
    for god in propagations:
        god_pos = (god[2], god[3])
        # 자신이 이미 전파를 당했다면, 이번 턴에 전파 불가
        if god_pos in propagated_to_this_turn:
            continue

        god_taste = taste[god_pos[0]][god_pos[1]]
        wish = trust[god_pos[0]][god_pos[1]] - 1
        d = trust[god_pos[0]][god_pos[1]] % 4
        trust[god_pos[0]][god_pos[1]] = 1 # 리더의 신앙심을 1로 설정

        current_x, current_y = god_pos
        
        while wish > 0:
            nx, ny = current_x + dx[d], current_y + dy[d]

            if not (0 <= nx < N and 0 <= ny < N):
                break

            current_x, current_y = nx, ny
            target_pos = (current_x, current_y)
            target_trust = trust[current_x][current_y]

            if set(taste[current_x][current_y]) == set(god_taste):
                continue

            # 전파가 일어났으므로, 대상을 '전파 당한 학생' 목록에 추가
            propagated_to_this_turn.add(target_pos)

            if wish > target_trust: # 강한 전파
                wish -= (target_trust + 1)
                trust[current_x][current_y] += 1
                taste[current_x][current_y] = list(god_taste)
            else: # 약한 전파
                current_taste_set = set(taste[current_x][current_y])
                for t in god_taste:
                    current_taste_set.add(t)
                taste[current_x][current_y] = sorted(list(current_taste_set))
                
                trust[current_x][current_y] += wish
                wish = 0

    answers = [0]*7
    for i in range(N):
        for j in range(N):
            s_taste = set(taste[i][j])
            val = trust[i][j]
            if s_taste == {'M', 'T', 'C'}: answers[0] += val
            elif s_taste == {'T', 'C'}: answers[1] += val
            elif s_taste == {'T', 'M'}: answers[2] += val
            elif s_taste == {'C', 'M'}: answers[3] += val
            elif s_taste == {'M'}: answers[4] += val
            elif s_taste == {'C'}: answers[5] += val
            elif s_taste == {'T'}: answers[6] += val

    for row in answers:
        print(row, end=" ")
    print()