def solution(n):
    # 1. 3진법으로 변환
    ternary = ""
    while n > 0:
        n, r = divmod(n, 3)
        ternary += str(r)   # 나머지를 뒤에 붙임 (뒤집힌 상태로 쌓임)

    # 2. ternary는 이미 뒤집힌 3진수 문자열
    # 3. 10진수로 변환
    return int(ternary, 3)