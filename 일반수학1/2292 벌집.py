"""def create_grouped_list(n):
    grouped_list = []
    current_number = 1
    group_sizes = [1]  # 첫 번째 그룹 크기

    # 다음 그룹 크기들 (6, 12, 18, ...)
    for i in range(1, (n // 6) + 1):
        group_sizes.append(i * 6)

    for size in group_sizes:
        if current_number > n:
            break
        group = []
        for _ in range(size):
            if current_number > n:
                break
            group.append(current_number)
            current_number += 1
        grouped_list.append(group)

    return grouped_list

def find_group_index(n, grouped_list):
    for index, group in enumerate(grouped_list):
        if n in group:
            return index + 1  # 인덱스는 0부터 시작하므로 1을 더해줌
    return -1  # 숫자 n이 리스트에 없을 경우

n = int(input())
n <= 1000000000
list = create_grouped_list(n)
print(find_group_index(n, list))"""

n = int(input())
room = 0
x = 0 # 거리별 증가량은 6의 배수
N = 1 # 초기 최대거리는 1

while True:
    room += 1 # 1번방부터 카운트 시작
    N = N + (6*x) # 최대길이마다 6의 배수로 증가함
    if n <= N : # 방번호와 최대 거리대비 방번호 비교
        print(room) # 최대 거리수안에 방번호가 있을 시 카운트 출력
        break
    else:
        x += 1 # 최대 거리수안에 방번호가 없으면 한칸 더 전진
