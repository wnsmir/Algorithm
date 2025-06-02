import copy

M, S = map(int, input().split())
fishs = []
for _ in range(M):
    fx, fy, d = map(int, input().split())
    fishs.append([fx - 1, fy - 1, d])  # 내부는 0-based로 저장
sx, sy = map(int, input().split())
shark = (sx - 1, sy - 1)
grid = [[0] * 4 for _ in range(4)]  # 물고기 냄새 격자 (0이면 냄새 없음)

def move_fishs(grid, fishs, shark):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    for idx in range(len(fishs)):
        x, y, d = fishs[idx]
        d -= 1  # 0~7 로 바꿔서 사용
        moved = False
        for i in range(8):
            nd = (d - i) % 8
            nx, ny = x + dx[nd], y + dy[nd]
            # “격자 안이고, 냄새 없다(==grid[nx][ny]==0), 상어가 아니다”
            if 0 <= nx < 4 and 0 <= ny < 4 and grid[nx][ny] == 0 and shark != (nx, ny):
                # 이동
                fishs[idx][0] = nx
                fishs[idx][1] = ny
                fishs[idx][2] = nd + 1  # 다시 1~8 방향으로
                moved = True
                break
        # i=0~7까지 못 간다면: (x,y)는 변하지 않고, 방향도 달라지지 않는다
        # fishs[idx][2]는 이미 원래의 방향(d+1)이므로 그대로 놔둠
    return fishs

def move_shark(shark, fishs):
    dir_map = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 순서 그대로: 상, 좌, 하, 우
    dir_num = [1, 2, 3, 4]

    def dfs(x, y, path, dirs):
        if len(dirs) == 3:
            all_paths.append((path[:], dirs[:]))
            return
        for d, (dx, dy) in enumerate(dir_map):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                path.append((nx, ny))
                dirs.append(dir_num[d])
                dfs(nx, ny, path, dirs)
                path.pop()
                dirs.pop()

    all_paths = []
    sx, sy = shark
    dfs(sx, sy, [], [])

    best_kill = -1
    best_dirs = None
    best_path = None
    best_dead_cells = None  # “죽은 좌표(cell)”를 저장
    best_dead_fish_indices = None  # “죽은 물고기 리스트 중에서 인덱스까지” 저장

    # fishs 는 [[x, y, d], …] 형태
    for path, dirs in all_paths:
        # path = [(x1,y1), (x2,y2), (x3,y3)]  (딱 3칸 이동)
        # dirs = [dir1, dir2, dir3]  (1~4 정수)
        dead_cells = set()
        dead_fish_idxs = []
        for idx, (fx, fy, _) in enumerate(fishs):
            # “fishs[idx]가 path 어딘가에 겹치면 죽음”
            if (fx, fy) in path:
                dead_cells.add((fx, fy))
                dead_fish_idxs.append(idx)
        kill_count = len(dead_fish_idxs)  # “한 칸에 물고기 3마리면 indices 리스트에 3번 들어가므로 3”

        # 사전순 비교 기준: kill_count 최대 → dirs를 문자열로 이어붙인 정수 비교
        if best_dirs is None:
            best_kill = kill_count
            best_dirs = dirs[:]
            best_path = path[:]
            best_dead_cells = dead_cells.copy()
            best_dead_fish_indices = dead_fish_idxs[:]
        else:
            if kill_count > best_kill:
                best_kill = kill_count
                best_dirs = dirs[:]
                best_path = path[:]
                best_dead_cells = dead_cells.copy()
                best_dead_fish_indices = dead_fish_idxs[:]
            elif kill_count == best_kill:
                # dirs 비교 (예: [1,2,3] → “123” vs best_dirs → 문자열 비교)
                cur_code = int(''.join(map(str, dirs)))
                best_code = int(''.join(map(str, best_dirs)))
                if cur_code < best_code:
                    best_dirs = dirs[:]
                    best_path = path[:]
                    best_dead_cells = dead_cells.copy()
                    best_dead_fish_indices = dead_fish_idxs[:]

    # best_path가 결정되었으면 실제로 상어 이동 → 마지막 칸이 상어 위치
    if best_path:
        shark = best_path[-1]

    # “best_dead_fish_indices” 를 이용해 fishs에서 실제로 죽은 물고기 전부 제거
    # 주의! 지우면 인덱스가 깨지므로, 역순으로 pop하거나 필터링
    if best_dead_fish_indices:
        # 필터 방식으로 간단하게 남은 것만 고르기
        new_fishs = []
        dead_set = set(best_dead_fish_indices)
        for idx, f in enumerate(fishs):
            if idx not in dead_set:
                new_fishs.append(f)
        fishs = new_fishs
    else:
        # 죽은 물고기 없음
        pass

    return shark, fishs, list(best_dead_cells)

def fish_smell(grid, dead_fishs):
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                grid[i][j] += 1
                if grid[i][j] == 3:  # 2턴이 지난 냄새
                    grid[i][j] = 0

    for (dx, dy) in dead_fishs:
        grid[dx][dy] = 1

    return grid

for _ in range(S):
    # 1) “복제 마법 시전” → 현재 fishs 전체를 deep copy
    duplicated = copy.deepcopy(fishs)

    # 2) 물고기 이동
    fishs = move_fishs(grid, fishs, shark)

    # 3) 상어 이동 → 물고기 몇 마리 죽였는지 계산, remove, shark 위치도 업데이트
    shark, fishs, dead_cells = move_shark(shark, fishs)

    # 4) 물고기 냄새 처리 (두 턴 지난 건 삭제, 방금 죽은 칸에 냄새 1로 설정)
    grid = fish_smell(grid, dead_cells)

    # 5) “복제 마법 완료” → step1에서 복제해 둔 fishs 전체를 지금 fishs 뒤에 붙인다
    fishs.extend(duplicated)

# 최종 남은 물고기 수 출력
print(len(fishs))