def solution(today, terms, privacies):
    idx = 1
    answer = []
    today = today.split(".")
    today = "".join(today)
    
    # 약관 : 기간 딕셔너리
    terms_dict = {}
    for term in terms:
        alpha, mon = term.split(" ")
        terms_dict[alpha] = mon
    
    # 회원정보에 약관기간 더하고 오늘날짜와 비교
    for pri in privacies:
        temp, term = pri.split(" ")
        year, mon, day = temp.split(".")
        # year, mon, day, term
        t = terms_dict[term]
        
        # 기간을 더했을때 12월이 넘어가면
        if int(mon) + int(t) > 12:
            plus_year = (int(mon) + int(t)) // 12
            mon = str((int(mon) + int(t)) % 12)
            if mon == '0':
                mon = '12'
                year = str(int(year) + plus_year -1)
            else:
                if len(mon) == 1:
                    mon = '0' + mon
                year = str(int(year) + plus_year)
        
        # 12개월이 넘지않는다면
        else:
            mon = str(int(mon) + int(t))
            if len(mon) == 1:
                mon = '0' + mon
        
        complete_date = "".join([year, mon, day])
        
        if int(today) >= int(complete_date):
            answer.append(idx)
            
        
        
        # 다음 사용자 정보 확인
        idx += 1
        
    return answer