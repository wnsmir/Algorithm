def solution(number, k):
    number = list(number)
    stack = []
    
    #첫번쨰 수 스택에 넣어주기
    stack.append(number[0])
    number.pop(0)
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    
    answer = ''
    for num in stack:
        answer += num
        
    return answer