from collections import deque

def solution(game_board, table):
    N = len(table)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x, y, grid, visited, flag):
        # 게임보드일때
        if flag == True:
            num = 0
        # 테이블일때
        else:
            num = 1

        queue = deque()
        queue.append((x, y))
        block = []
        block.append((x, y))
        # ✅ 시작점 방문 표시 (외부 visited에 그대로 반영)
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    # ✅ 넘겨받은 visited만 사용
                    if grid[nx][ny] == num and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        block.append((nx, ny))

        # 블록 한조각 반환
        return block

    def normalize(blocks):
        normalized_blocks = []
        min_x = float('inf')
        min_y = float('inf')

        for block in blocks:
            x, y = block
            if min_x > x:
                min_x = x
            if min_y > y:
                min_y = y
        for block in blocks:
            x, y = block
            normalized_blocks.append((x - min_x, y - min_y))

        return normalized_blocks

    def rotate(blocks):
        rotated_blocks = []
        for block in blocks:
            x, y = block
            rotated_blocks.append((-y, x))
        return rotated_blocks

    # ✅ 정규화 + 정렬 + 튜플(표준형)
    def canon(blocks):
        return tuple(sorted(normalize(blocks)))

    table_visited = [[False]*N for _ in range(N)]

    # table에 있는 조각들 blocks에 추가
    blocks = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and not table_visited[i][j]:
                blocks.append(bfs(i, j, table, table_visited, False))

    answer = 0

    # game_board 빈공간들에 정규화 + 회전한 조각들 대입
    game_board_visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and not game_board_visited[i][j]:
                blank_block = bfs(i, j, game_board, game_board_visited, True)
                blank_canon = canon(blank_block)

                for b in range(len(blocks) - 1, -1, -1):
                    block = blocks[b]
                    c0 = canon(block)
                    
                    b90 = rotate(block)
                    c90 = canon(b90)
                    
                    b180 = rotate(b90)
                    c180 = canon(b180)
                    
                    b270 = rotate(b180)
                    c270 = canon(b270)

                    if blank_canon in (c0, c90, c180, c270):
                        answer += len(block)
                        blocks.pop(b)
                        break

    return answer