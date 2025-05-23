def solution(bandage, health, attacks):
    max_health = health
    count = 0
    idx = 0
    time = 0
    
    for i in range(1, attacks[-1][0]+1):
        time += 1
        #해당 턴에 공격이 있다면
        if attacks[idx][0] == time:
            health -= attacks[idx][1]
            idx += 1
            count = 0
            #공격받고 체력이 0이하로 내려가면 죽음
            if health <= 0:
                return -1
            
        #공격이 없다면
        else:
            #이번턴 회복
            health += bandage[1]
            count += 1
            if health > max_health:
                health = max_health
            #count가 t라면 추가회복
            if count == bandage[0]:
                health += bandage[2]
                count = 0
                if health > max_health:
                    health = max_health
        print(health)
        
    return health