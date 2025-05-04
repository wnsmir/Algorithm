from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_set = set()
    
    # 모든 길이의 순열을 만든다
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            num_set.add(num)
    
    # 소수만 카운트
    count = 0
    for num in num_set:
        if is_prime(num):
            count += 1

    return count