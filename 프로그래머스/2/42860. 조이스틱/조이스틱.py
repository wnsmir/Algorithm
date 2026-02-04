def solution(name):
    na = ''
    for i in range(len(name)):
        na += "A"

    # 마지막으로 A가 아닌 수의 위치
    count = 0
    a_count = 0
    for ch in name:
        if ch != "A":
            diff = ord(ch) - ord("A")
            count += 1

            if a_count > 0:
                count += a_count
                a_count = 0
        else:
            a_count += 1

    f_answer = 0
    # 먼저 상하값만 따로 더해주기
    for ch in name:
        if ch != "A":
            diff = ord(ch) - ord("A")
            f_answer += min(diff, 26 - diff)

    n = len(name)  # ✅ n이 없어서 문법/NameError 발생하던 부분 수정

    min_min_root = float('inf')

    for i in range(n):
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1

        no_change = n - 1
        change1 = 2 * i + (n - j)
        change2 = i + 2 * (n - j)

        min_root = min(no_change, change1, change2)
        min_min_root = min(min_min_root, min_root)

    return min_min_root + f_answer