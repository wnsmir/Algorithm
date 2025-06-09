N = int(input())
blocks = []
for i in range(N):
    t, x, y = map(int, input().split())
    blocks.append((t, x, y))

point = 0

#파란색 영역
blue = [[0]*6 for _ in range(4)]
green = [[0]*6 for _ in range(4)]

def delete_blue(col):
    #blue 보드에서 col열 삭제 후 왼쪽으로 당김
    for r in range(4):
        for c in range(col, 0, -1):
            blue[r][c] = blue[r][c-1]
        blue[r][0] = 0

def delete_green(col):
    #blue 보드에서 col열 삭제 후 왼쪽으로 당김
    for r in range(4):
        for c in range(col, 0, -1):
            green[r][c] = green[r][c-1]
        green[r][0] = 0

def check_blue():
    global point

    while True:
        full_line = -1
        for y in range(2, 6):
            count = 0
            for x in range(4):
                if blue[x][y] == 1:
                    count += 1
            if count == 4:
                full_line = y
                delete_blue(full_line)
                point += 1
     
        if full_line == -1:
            break
            
def check_green():
    global point

    while True:
        full_line = -1
        for y in range(2, 6):
            count = 0
            for x in range(4):
                if green[x][y] == 1:
                    count += 1
            if count == 4:
                full_line = y
                delete_green(full_line)
                point += 1
     
        if full_line == -1:
            break


for i in range(N):
    t, x, y = blocks[i]

    #t가 1이면 x, y에 하나 배치
    if t == 1:
        #연한 구간에 배치하고
        nx, ny = x, 0
        #앞에 다른블록이 있거나 경계까지 오른쪽으로 이동
        while ny + 1 < 6 and blue[nx][ny + 1] == 0:
            ny += 1
        #만약 멈춘곳이 연한 파란색이라면
        if ny == 1:
            #5번쨰 열 삭제후 한칸씩 밀기
            delete_blue(5)
            #2열에 배치
            blue[nx][2] = 1
        else:
            blue[nx][ny] = 1
        
    #t가 2라면 x, y에 가로로 배치
    if t == 2:
        nx, ny = x, 1
        while ny + 1 < 6 and blue[nx][ny + 1] == 0:
            ny += 1
        #멈춘곳이 1열이면 2칸 밀고 2 3열에 배치
        if ny == 1:            
            delete_blue(5)
            delete_blue(5)
            #2, 3열에 배치
            blue[nx][2] = 1
            blue[nx][3] = 1      

        #멈춘곳이 2열이면 한칸밀고 2 3열에 배치
        elif ny == 2:
            blue[nx][2] = 1
            county = 0
            for x in range(4):
                if blue[x][2] == 1:
                    county += 1
            if county == 4:
                check_blue()
                blue[nx][2] = 1
            else:
                delete_blue(5)
                #2, 3열에 배치
                blue[nx][2] = 1
                blue[nx][3] = 1       
        else:
            blue[nx][ny] = 1   
            blue[nx][ny-1] = 1          
        
    #t가 3이라면 x, y에 세로로 배치
    if t == 3:
        nx, nx2, ny = x, x +1, 0
        while ny + 1 < 6 and blue[nx][ny + 1] == 0 and blue[nx2][ny + 1] == 0:
            ny += 1
        #만약 멈춘곳이 연한 파란색이라면
        if ny == 1:
            delete_blue(5)
            #2열에 배치
            blue[nx][2] = 1
            blue[nx2][2] = 1
        else:
            blue[nx][ny] = 1
            blue[nx2][ny] = 1
    
    check_blue()

for i in range(N):
    t, x, y = blocks[i]

    #t가 1이면 x, y에 하나 배치
    if t == 1:
        #연한 구간에 배치하고
        nx, ny = abs(3-y), 0
        #앞에 다른블록이 있거나 경계까지 오른쪽으로 이동
        while ny + 1 < 6 and green[nx][ny + 1] == 0:
            ny += 1
        #만약 멈춘곳이 연한 파란색이라면
        if ny == 1:
            #5번쨰 열 삭제후 한칸씩 밀기
            delete_green(5)
            #2열에 배치
            green[nx][2] = 1
        else:
            green[nx][ny] = 1
        
    #t가 3라면 x, y에 가로로 배치
    if t == 3:
        nx, ny = abs(y-3), 1
        while ny + 1 < 6 and green[nx][ny + 1] == 0:
            ny += 1
        #멈춘곳이 1열이면 2칸 밀고 2 3열에 배치
        if ny == 1:            
            delete_green(5)
            delete_green(5)
            #2, 3열에 배치
            green[nx][2] = 1
            green[nx][3] = 1      

        #멈춘곳이 2열이면 한칸밀고 2 3열에 배치
        elif ny == 2:
            green[nx][2] = 1
            county = 0
            for x in range(4):
                if green[x][2] == 1:
                    county += 1
            if county == 4:
                check_green()
                green[nx][2] = 1
            else:
                delete_green(5)
                #2, 3열에 배치
                green[nx][2] = 1
                green[nx][3] = 1  
        else:
            green[nx][ny] = 1   
            green[nx][ny-1] = 1          
        
    #t가 2이라면 x, y에 세로로 배치
    if t == 2:
        nx, nx2, ny = 3-y, 3-(y+1), 0
        while ny + 1 < 6 and green[nx][ny + 1] == 0 and green[nx2][ny + 1] == 0:
            ny += 1
        #만약 멈춘곳이 연한 파란색이라면
        if ny == 1:
            delete_green(5)
            #2열에 배치
            green[nx][2] = 1
            green[nx2][2] = 1
        else:
            green[nx][ny] = 1
            green[nx2][ny] = 1
    
    check_green()


answer = 0
print(point)
for x in range(4):
    for y in range(6):
        if blue[x][y] == 1:
            answer += 1
for x in range(4):
    for y in range(6):
        if green[x][y] == 1:
            answer += 1
print(answer)