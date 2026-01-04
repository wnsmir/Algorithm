def solution(new_id):
    
    # 1단계 : 소문자 치환
    new_id = new_id.lower()

    new_id = list(new_id)

    # 2단계 : 소문자, 숫자, -, _, . 를 제외한 모든 문자열 제거
    word_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3','4','5','6','7','8','9', '-','_','.']
    real_new_id = ''
    for char in new_id:
        if char in word_list:
            real_new_id += char
    
    new_id = list(real_new_id)
    print(new_id)
    # 3단계 ..를 .로 치환
    i = 0
    count = 0
    while i < len(new_id):
        if new_id[i] == '.':
            count += 1
        else:
            count = 0

        if count == 2:
            new_id.pop(i)   # 현재 위치 삭제
            count = 1       # '.' 하나는 남아있으니 1로
            continue        # i 증가하지 말고 같은 i 재검사

        i += 1
    
    # 4단계 .이 처음이나 끝에 위치한다면 제거
    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop()
    
    # 5단계 빈문자열이 되면 a를 대입
    if len(new_id) == 0:
        new_id.append('a')
    
    # 6단계 길이가 16이상이면 15개 이후로 다 제거, 제거후 15번째가 .이면 마침표도 제거
    if len(new_id) > 15:
        new_id = new_id[0:15]
    while new_id[-1] == '.':
        new_id.pop()
        
    # 7단계 : len이 2이하라면 3될때까지 마지막문자 대입
    while len(new_id) < 3:
        new_id.append(new_id[-1])
    
    answer = ''.join(new_id)
    return answer