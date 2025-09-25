import itertools

def solution(friends, gifts):
    
    # 다음달 선물받을 개수저장
    answer = {}
    for friend in friends:
        answer[friend] = 0
    
    for i in range(len(gifts)):
        gifts[i] = gifts[i].split()
    
    # 선물 보낸사람 저장
    send = {}
    for friend in friends:
        send[friend] = []
    
    # 선물 받은 개수 저장
    recieve = {}
    for friend in friends:
        recieve[friend] = 0
    
    for giver, reciever in gifts:
        # 주는사람 준 선물 count
        send[giver].append(reciever)
        # 받는사람 받은선물 count
        recieve[reciever] += 1
                    
    # 지수 설정
    compare = {}
    for i in range(len(friends)):
        compare[friends[i]] = len(send[friends[i]]) - recieve[friends[i]]
        
        
    for p in itertools.combinations(friends, 2):
        giver, reciever = p
        # a, b의 주고 받은 선물 수 비교
        give = send[giver].count(reciever)
        get = send[reciever].count(giver)
        
        # a가 b보다 많이 줬다면
        if give > get:
            answer[giver] += 1
        
        # b가 a보다 많이 줬다면
        elif give < get:
            answer[reciever] += 1
    
        # 같다면 지수비교
        else:
            # a가 지수가 더 크면 a가 받기
            if compare[giver] > compare[reciever]:
                answer[giver] += 1
            # b가 더 크다면
            elif compare[giver] < compare[reciever]:
                answer[reciever] += 1
            # 지수도 같다면 pass
            else:
                continue
                
    real_answer = []          
    for key in answer:
        real_answer.append(answer[key])
        
    return max(real_answer)