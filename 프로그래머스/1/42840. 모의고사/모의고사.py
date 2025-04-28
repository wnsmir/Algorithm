def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    f = s = t = 0  # 1번, 2번, 3번 수포자 맞힌 개수
    
    for index in range(len(answers)):
        if answers[index] == one[index % len(one)]:
            f += 1
        if answers[index] == two[index % len(two)]:
            s += 1
        if answers[index] == three[index % len(three)]:
            t += 1
    
    max_score = max(f, s, t)  # 가장 높은 점수
    answer = []
    
    if f == max_score:
        answer.append(1)
    if s == max_score:
        answer.append(2)
    if t == max_score:
        answer.append(3)
        
    return answer