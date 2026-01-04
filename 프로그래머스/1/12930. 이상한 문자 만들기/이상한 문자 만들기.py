def solution(s):
    answer = []
    words = s.split(" ")
    for s in words:
        s = list(s)
        for i in range(len(s)):
            i += 1
            # 홀수번째면
            if i%2 != 0:
                s[i-1] = s[i-1].upper()
            else:
                s[i-1] = s[i-1].lower()       
        s = ''.join(s)
        answer.append(s)
    answer = " ".join(answer)
    
    return answer