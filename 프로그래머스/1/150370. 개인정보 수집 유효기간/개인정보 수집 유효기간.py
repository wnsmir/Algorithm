def solution(today, terms, privacies):
    t_year, t_month, t_day = map(int, today.split("."))
    i = 0
    answer = []

    for pri in privacies:
        i += 1
        date, term = pri.split(" ")
        year, month, day = map(int, date.split("."))

        # 약관개월 찾기 (원래 구조 유지)
        plus_month = 0
        for ter in terms:
            t, time = ter.split(' ')
            if term == t:
                plus_month = int(time)
                break  # ✅ 찾았으면 바로 종료(미세 최적화 + 안전)

        # ----------------------------
        # ✅ (1) 월 더하기를 정확히 처리 (최대 100개월)
        # ----------------------------
        month += plus_month
        year += (month - 1) // 12          # ✅ 여러 해 반영
        month = (month - 1) % 12 + 1       # ✅ 1~12로 정규화

        # ----------------------------
        # ✅ (2) 만료일은 하루 전까지 보관 가능 => day - 1
        # ----------------------------
        day -= 1
        if day == 0:                       # ✅ 0일이면 전 달 28일
            day = 28
            month -= 1
            if month == 0:
                month = 12
                year -= 1

        # ----------------------------
        # 오늘 날짜와 비교 (원래 구조 유지)
        # ----------------------------
        if year < t_year:
            answer.append(i)
        elif year == t_year:
            if month < t_month:
                answer.append(i)
            elif month == t_month:
                if day < t_day:            # ✅ "오늘부터 파기"라서 day < 오늘일이면 파기
                    answer.append(i)

    return answer