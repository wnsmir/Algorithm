def solution(info, query):
    # 학생 정보 파싱
    students = [s.split() for s in info]
    for s in students:
        s[4] = int(s[4])  # 점수를 int로

    # 쿼리 파싱 ("and" 기준 분리 + 마지막 '푸드 점수' 분리)
    querys = []
    for q in query:
        parts = q.split(" and ")
        last_part = parts[-1].split()  # 예: "pizza 100" -> ["pizza", "100"]
        parts[-1] = last_part[0]
        parts.append(int(last_part[1]))  # 점수는 int
        querys.append(parts)

    # 쿼리 개수만큼 결과 배열 준비
    result = [0] * len(querys)

    # 각 쿼리별로 학생 대조
    for qi, que in enumerate(querys):
        cnt = 0
        for student in students:
            Flag = True

            # 언어
            if not (que[0] == student[0] or que[0] == '-'):
                Flag = False
            # 직군
            if not (que[1] == student[1] or que[1] == '-'):
                Flag = False
            # 경력
            if not (que[2] == student[2] or que[2] == '-'):
                Flag = False
            # 소울푸드
            if not (que[3] == student[3] or que[3] == '-'):
                Flag = False
            # 점수 (학생 점수 >= 쿼리 최소 점수)
            if not (student[4] >= que[4]):
                Flag = False

            if Flag:
                cnt += 1

        result[qi] = cnt

    return result