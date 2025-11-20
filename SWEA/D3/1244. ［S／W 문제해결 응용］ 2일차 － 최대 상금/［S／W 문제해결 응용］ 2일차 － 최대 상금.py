def dfs(num, cnt):
    global ans, N, visited

    # 종료 조건
    if cnt == N:
        ans = max(ans, int(num))
        return
    
    if (num, cnt) in visited:
        return
    
    visited.add((num, cnt))
    lst = list(num)
    L = len(lst)

    for i in range(L):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]
            dfs(''.join(lst), cnt + 1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
tc = 0
for _ in range(T):
    tc += 1
    num, N = input().split()
    N = int(N)
    ans = 0
    visited = set()
    dfs(num, 0)
    print(f"#{tc} {ans}")