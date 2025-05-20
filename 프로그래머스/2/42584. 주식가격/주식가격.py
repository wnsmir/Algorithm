def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 스택에 있는 값보다 작아지면 해당 시간까지 유지됨
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 끝까지 가격이 떨어지지 않은 것 처리
    for i in stack:
        answer[i] = n - i - 1

    return answer