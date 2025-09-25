def solution(new_id):
    
    # 1단계 소문자 만들기
    new_id = new_id.lower()
    # 2단계 알파벳, 숫자, -, _, . 빼고 모든문자 제거
    new_id = list(new_id)
    legend = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-', '_', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in range(len(new_id) -1, -1, -1):
        if new_id[i] not in legend:
            del new_id[i]
    
    # 3 .이 연속으로 2개나오면 하나로
    flag = True
    last = ''
    while flag == True:
        flag = False
        for i in range(len(new_id)):
            if new_id[i] == '.' and last == '.':
                del new_id[i]
                flag = True
                break
            else:
                last = new_id[i]

    # 4 .가 처음에 있거나 마지막에 있으면 삭제
    if new_id and new_id[-1] == '.':
        del new_id[-1]
    if new_id and new_id[0] == '.':
        del new_id[0]
    
    # 5 빈문자열이면 'a'넣기
    if len(new_id) == 0:
        new_id.append('a')
    
    # 6 16이상 제거, 15가 . 면 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()
    
    # 7 길이가 2 이하라면 마지막문자 3까지 반복
    while len(new_id) < 3:
        new_id.append(new_id[-1])
    
    answer = ''.join(new_id)
    return answer