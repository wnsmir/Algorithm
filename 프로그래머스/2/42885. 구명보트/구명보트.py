def solution(people, limit):
    # people 정렬
    # 가장 무거운사람 + 가장 가벼운사람 limit과 비교
    people = sorted(people)
    answer = 0

    # ✅ 삭제 대신 인덱스만 이동
    left = 0
    right = len(people) - 1

    while True:
        # people이 다 빌때까지  (left > right면 다 처리된 상태)
        if right - left + 1 > 1:   # len(people[left:right+1]) > 1 과 같은 의미
            sum_people = people[right] + people[left]

            # limit보다 합이 크면 혼자탑승 (무거운 사람만)
            if limit < sum_people:
                right -= 1
                answer += 1

            # limit보다 합이 작거나 같으면 가장 작은사람과 합승
            else:
                right -= 1
                left += 1
                answer += 1

                # 두개남아서 다 탔으면 종료 (인덱스가 교차하면 끝)
                if left > right:
                    return answer

        # people에 사람이 한명 남았으면 answer += 1하고 종료
        elif right - left + 1 == 1:
            answer += 1
            return answer

        # (안전장치) 아무도 안 남은 경우
        else:
            return answer