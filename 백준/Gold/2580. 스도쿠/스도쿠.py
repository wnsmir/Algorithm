import sys
input = sys.stdin.readline

# 1) 입력 받으면서 board, rows, cols, boxes, empties 구성
board = [list(map(int, input().split())) for _ in range(9)]
rows = [set(range(1,10)) for _ in range(9)]
cols = [set(range(1,10)) for _ in range(9)]
boxes= [set(range(1,10)) for _ in range(9)]
empties = []

for r in range(9):
    for c in range(9):
        v = board[r][c]
        if v:
            rows[r].remove(v)
            cols[c].remove(v)
            boxes[(r//3)*3 + (c//3)].remove(v)
        else:
            empties.append((r,c))

# 2) DFS 함수: 빈 칸이 없으면 True 반환
def dfs():
    if not empties:
        return True

    # 남은 빈 칸 중 후보 수가 가장 적은 칸을 선택
    best = min(
        empties,
        key=lambda x: len(rows[x[0]] & cols[x[1]] & boxes[(x[0]//3)*3 + (x[1]//3)])
    )
    r, c = best
    b = (r//3)*3 + (c//3)
    candidates = rows[r] & cols[c] & boxes[b]  # 후보 숫자 집합

    if not candidates:
        return False

    empties.remove(best)
    for v in candidates:
        # 배치
        board[r][c] = v
        rows[r].remove(v)
        cols[c].remove(v)
        boxes[b].remove(v)

        if dfs():
            return True

        # 되돌리기
        board[r][c] = 0
        rows[r].add(v)
        cols[c].add(v)
        boxes[b].add(v)

    empties.append(best)
    return False

# 3) 실행 및 출력
dfs()
out = []
for row in board:
    out.append(" ".join(map(str, row)))
sys.stdout.write("\n".join(out))