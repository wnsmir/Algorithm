def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        part = a[i] * b[i]
        answer += part

    return answer