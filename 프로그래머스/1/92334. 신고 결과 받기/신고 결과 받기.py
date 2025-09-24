def solution(id_list, report, k):
    result = []
    
    # 유저아이디 딕셔너리 생성 : 신고한 사람 저장용도
    user_id = {}
    for id in id_list:
        user_id[id] = []
        
    # 신고대상자 딕셔너리 생성 : 신고받은 횟수 저장용도
    user_report = {}
    for id in id_list:
        user_report[id] = 0
    
    # report를 순회하면서 신고대상자 스택 +1, 유저 딕셔너리에 대상자 이름 추가
    for re in report:
        name, report_name = re.split()
        
        # 이미 해당유저가 신고한 사람이면 continue
        if report_name in user_id[name]:
            continue
        else:
            user_id[name].append(report_name)
            user_report[report_name] += 1
    
    # k가 넘는 신고대상자 list에 추가, 유저딕셔너리 순회하면서 대상자이름 있으면 result에 +1
    stop_user = []
    for name in id_list:
        # k보다 신고횟수가 크다면
        if user_report[name] >= k:
            stop_user.append(name)
    
    for name in user_id:
        count = 0
        # 신고한 사람이 정지리스트에 있다면
        for user in stop_user:
            if user in user_id[name]:
                count += 1
            
        result.append(count)
    
    return result