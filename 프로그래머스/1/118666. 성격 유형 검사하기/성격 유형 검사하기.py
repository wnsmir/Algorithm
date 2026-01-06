from collections import defaultdict


def solution(survey, choices):
    point = defaultdict(int)
    answer = ''
    typ = ["R", "C", "J", "A", "T", "F", "M", "N"]
    
    legend_choice = defaultdict(int)
    for i in range(7):
        legend_choice[i] = abs(3-i)

    for t in typ:
        point[t] = 0

    for i in range(len(survey)):
        if choices[i] < 4:
            point[survey[i][0]] += legend_choice[choices[i]-1]
        elif choices[i] > 4:
            point[survey[i][1]] += legend_choice[choices[i]-1]
    
    if point["R"] > point["T"]:
        answer += "R"
    elif point["R"] < point["T"]:
        answer += "T"
    else:
        answer += "R"
        
    if point["C"] > point["F"]:
        answer += "C"
    elif point["C"] < point["F"]:
        answer += "F"
    else:
        answer += "C"

    if point["J"] > point["M"]:
        answer += "J"
    elif point["J"] < point["M"]:
        answer += "M"
    else:
        answer += "J"
    
    if point["A"] > point["N"]:
        answer += "A"
    elif point["A"] < point["N"]:
        answer += "N"
    else:
        answer += "A"
    
    return answer