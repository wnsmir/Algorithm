import itertools

def solution(numbers):
    s = set()
    answer = []
    
    co = itertools.combinations(numbers, 2)
    for c in co:
        one, two = c
        s.add(one + two)
    
    print(s)
    
    for num in s:
        answer.append(num)

    return sorted(answer)