from collections import defaultdict

def solution(survey, choices):
    result = ""
    score = defaultdict(list)
    keys = ["R", "T", "C", "F", "J", "M", "A", "N"]
    for key in keys:
        score[key] = []
    
    for i in range(len(choices)):
        # 점수가 4이 넘으면 오른쪽 원소에 점수추가
        if choices[i] > 4:
            score[survey[i][1]].append(choices[i]-4)
            
        # 점수가 4보다 낮으면 왼쪽 원소에 점수추가
        elif choices[i] < 4:
            score[survey[i][0]].append(4-choices[i])
        
    print(score)
    # score에 점수 모두 더해주기
    for key in keys:
        score[key] = sum(score[key])
    
    # 1유형 비교
    if score["R"] > score["T"]:
        result += "R"
    elif score["R"] < score["T"]:
        result += "T"
    else:
        result += "R"
    
    # 2유형 비교
    if score["C"] > score["F"]:
        result += "C"
    elif score["C"] < score["F"]:
        result += "F"
    else:
        result += "C"
    
    # 3유형 비교
    if score["J"] > score["M"]:
        result += "J"
    elif score["J"] < score["M"]:
        result += "M"
    else:
        result += "J"
    
    # 4유형 비교
    if score["A"] > score["N"]:
        result += "A"
    elif score["A"] < score["N"]:
        result += "N"
    else:
        result += "A"
        
    return result