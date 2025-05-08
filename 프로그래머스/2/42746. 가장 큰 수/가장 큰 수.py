def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 핵심: 두 숫자를 이어붙인 값을 기준으로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 예외 처리: 가장 큰 숫자가 0이면 (ex. [0, 0, 0])
    if numbers[0] == '0':
        return '0'
    
    # 정렬된 숫자들을 이어붙여서 반환
    return ''.join(numbers)