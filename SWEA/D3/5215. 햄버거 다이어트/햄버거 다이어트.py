T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())  # N: 재료 수, L: 제한 칼로리

    items = []
    for _ in range(N):
        t, k = map(int, input().split())  # t: 맛 점수, k: 칼로리
        items.append((t, k))

    # dp[c] = 칼로리 c 이내에서 얻을 수 있는 최대 맛 점수
    dp = [0] * (L + 1)

    # 0/1 배낭 DP (각 재료는 한 번만 사용 가능)
    for t, k in items:
        # 같은 재료 여러 번 쓰지 않도록 역순으로 순회
        for c in range(L, k - 1, -1):
            dp[c] = max(dp[c], dp[c - k] + t)

    answer = dp[L]
    print(f"#{tc} {answer}")