def solution(numbers):
    answer = []
    for i in range(1, 10):
        if i not in numbers:
            answer.append(i)
    
    answer = sum(answer)
    return answer