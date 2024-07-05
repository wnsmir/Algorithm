def most_frequent_alphabet(word):
    # 모든 문자를 소문자로 변환
    word = word.lower()
    
    # 알파벳 빈도를 저장할 딕셔너리 초기화
    frequency = {}
    
    # 각 알파벳의 빈도 계산
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # 가장 높은 빈도를 찾기
    max_freq = 0
    most_frequent_char = ''
    multiple_max = False
    
    for char, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_char = char
            multiple_max = False
        elif freq == max_freq:
            multiple_max = True
    
    # 가장 많이 사용된 알파벳이 여러 개인 경우
    if multiple_max:
        return '?'
    else:
        # 대문자로 변환하여 반환
        return most_frequent_char.upper()

# 입력 받기
word = input().strip()

# 결과 출력
print(most_frequent_alphabet(word))
