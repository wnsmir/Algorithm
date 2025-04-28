T = int(input())
for _ in range(T):
    m = int(input())
    Q = m//25
    D = (m - Q*25) // 10
    N = (m - Q*25 - D*10) // 5
    P = (m - Q*25 - D*10 - N*5)
    print(Q,D,N,P,sep=' ')