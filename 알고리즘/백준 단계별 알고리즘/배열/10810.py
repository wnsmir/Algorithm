N, M = map(int, input().split())  # 리스트의 크기 N과 명령의 수 M을 입력받음
b = [0] * N  # 크기 N의 리스트를 0으로 초기화

for _ in range(M):
    i, j, k = map(int, input().split())  # 시작 인덱스 i, 끝 인덱스 j, 값 k를 입력받음
    for index in range(i-1, j):  # 인덱스 i-1부터 j-1까지 리스트의 값을 k로 설정
        b[index] = k

for value in b:  # 리스트 b의 값을 공백으로 구분하여 출력
    print(value, end=" ")