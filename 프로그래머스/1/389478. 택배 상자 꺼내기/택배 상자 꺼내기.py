def solution(n, w, num):
    length = n // w
    if n % w != 0:
        length += 1

    boxes = [[0] * w for _ in range(length)]

    k = 1
    for i in range(length):
        for j in range(w):
            jj = j if i % 2 == 0 else (w - 1 - j)

            if k == n + 1:
                k = 0
            boxes[i][jj] = k

            if k != 0:
                k += 1

    answer = 0

    for i in range(length):
        for j in range(w):
            if boxes[i][j] == num:
                ii = i  # ✅ i 대신 ii로 아래쪽 탐색
                while ii < length:
                    if boxes[ii][j] != 0:
                        answer += 1
                    ii += 1
                return answer  # ✅ num 찾았으면 바로 종료

    return 0