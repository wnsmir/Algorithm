def solution(s):
    word = []
    answer = []
    
    for ch in s:
        if ch.isdigit() == True:
            answer.append(ch)
            
        else:
            word.append(ch)
            check = ''.join(word)

            if check == 'zero':
                answer.append('0')
                word =[] 
            elif check == 'one':
                answer.append('1')
                word = []
            elif check == 'two':
                answer.append('2')
                word = []
                
            elif check == 'three':
                answer.append('3')
                word = []
                
            elif check == 'four':
                answer.append('4')
                word = []
                
            elif check == 'five':
                answer.append('5')
                word = []
                
            elif check == 'six':
                answer.append('6')
                word = []
                
            elif check == 'seven':
                answer.append('7')
                word = []
                
            elif check == 'eight':
                answer.append('8')
                word = []
                
            elif check == 'nine':
                answer.append('9')
                word = []
                
    answer = ''.join(answer)
    return int(answer)