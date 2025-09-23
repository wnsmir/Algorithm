def solution(n, w, num):
    m = n//w +1
    boxes = [[0]*w for _ in range(m)]
    count = 0
    
    # 각 층마다
    for i in range(m):
        # 홀수층이면 반대로 쌓기
        if i%2 != 0:
            for j in range(w-1, -1, -1):
                count += 1
                if count > n:
                    break
                else:
                    boxes[i][j] = count
            
        else:
            for j in range(w):
                count += 1
                if count > n:
                    break
                else:
                    boxes[i][j] = count
    
    # num 위치찾기
    x, y = 0, 0
    for i in range(m):
        for j in range(w):
            if boxes[i][j] == num:
                x, y = i, j
    
    box = 0
    for i in range(x, m):
        # 마지막칸이 비어있으면 바로 출력
        if boxes[i][y] == 0:
            return box
        # 마지막칸에 도착하면 +1 더해주고 출력
        elif i == m-1:
            return box + 1
        # 다음칸에 박스가 있으면 +1
        else:
            box += 1