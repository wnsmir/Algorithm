def solution(dartResult):
    dart_count = 0
    dart = {}
    dart[0] = 0
    answer = 0
    
    for i in range(len(dartResult)):
        option = ''
        # 다트기회라면
        if dartResult[i].isdigit():
            dart_count += 1
            # 10일때
            if dartResult[i+1].isdigit():
                dart_score = int(dartResult[i] + dartResult[i+1])
                area = area = dartResult[i+2]
                dartResult = list(dartResult)
                dartResult[i+1] = 'i'
                dartResult = ''.join(dartResult)
                if i+3 < len(dartResult) and not dartResult[i+3].isdigit():
                    # 그 다음은 옵션
                    option = dartResult[i+3]
            # 한자리 수 일때
            else:
                dart_score = int(dartResult[i])
                area = dartResult[i+1]
                # 다다음이 숫자가 아니고 끝이 아니라면
                if i+2 < len(dartResult) and not dartResult[i+2].isdigit():
                    # 그 다음은 옵션
                    option = dartResult[i+2]
                
            # area와 option으로 계산하기
            if area == 'S':
                dart[dart_count] = dart_score
                
            elif area == 'D':
                dart[dart_count] = dart_score * dart_score
                
            elif area == 'T':
                dart[dart_count] = dart_score * dart_score * dart_score
                
            if option == '*':
                dart[dart_count -1] *= 2
                dart[dart_count] *= 2
                
            elif option == '#':
                dart[dart_count] *= -1
    
    for i in range(len(dart)):
        answer += dart[i]

    return answer