def solution(dartResult):
    scores = []
    i = 0
    n = len(dartResult)

    while i < n:
        ch = dartResult[i]

        # 1) 숫자 처리 (0~10)
        if ch.isdigit():
            # 10 처리
            if ch == '1' and i + 1 < n and dartResult[i + 1] == '0':
                scores.append(10)
                i += 2
            else:
                scores.append(int(ch))
                i += 1

        # 2) 보너스 처리 (S/D/T) -> 방금 점수에 적용
        elif ch in ('S', 'D', 'T'):
            if ch == 'S':
                scores[-1] = scores[-1] ** 1
            elif ch == 'D':
                scores[-1] = scores[-1] ** 2
            else:  # 'T'
                scores[-1] = scores[-1] ** 3
            i += 1

        # 3) 옵션 처리 (*, #) -> 방금 점수(및 이전 점수)에 적용
        elif ch in ('*', '#'):
            if ch == '*':
                scores[-1] *= 2
                if len(scores) >= 2:
                    scores[-2] *= 2
            else:  # '#'
                scores[-1] *= -1
            i += 1

    return sum(scores)