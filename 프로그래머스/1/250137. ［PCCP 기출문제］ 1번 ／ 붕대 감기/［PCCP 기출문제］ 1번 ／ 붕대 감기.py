def solution(bandage, health, attacks):
    
    time_limit = bandage[0]
    heal = bandage[1]
    plus = bandage[2]
    health_count = 0
    cur_health = health
    
    # 마지막 공격턴까지 반복 진행
    for i in range(attacks[-1][0] + 1):
        # 이번턴에 공격이 있는가?
        check = False
        for attack in attacks:
            attack_time = attack[0]
            attack_damage = attack[1]
            # 공격타임이 현재턴이면
            if attack_time == i:
                check = True
                # 공격력만큼 체력감소
                cur_health -= attack_damage
                if cur_health <= 0:
                    return -1
                health_count = 0
            
        # 이번턴에 공격이 없었다면
        if check == False:
            health_count += 1
            cur_health += heal
            if cur_health >= health:
                cur_health = health
            # 최대 시간으로 회복했다면
            if health_count == time_limit:
                cur_health += plus
                health_count = 0
                if cur_health >= health:
                    cur_health = health

    return cur_health