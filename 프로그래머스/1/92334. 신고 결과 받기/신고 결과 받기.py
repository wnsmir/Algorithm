def solution(id_list, report, k):
    
    d = {}
    for id in id_list:
        d[id] = set()
        
    for re in report:
        reporter, people = re.split(" ")
        d[people].add(reporter)
    
    stopped = []
    
    for i in range(len(id_list)):
        # 2회 이상 신고받아서 정지된다면
        if len(d[id_list[i]]) >= k:
            stopped.append(id_list[i])         
    
    check = {id: set() for id in id_list}
    for re in report:
        reporter, people = re.split(" ")
        check[reporter].add(people)
    
    answer = []
    
    for i in range(len(id_list)):
        temp = 0
        for name in stopped:
            # 신고한 사람이 정지리스트에 있다면
            if name in check[id_list[i]]:
                temp += 1
        answer.append(temp)
    
    return answer