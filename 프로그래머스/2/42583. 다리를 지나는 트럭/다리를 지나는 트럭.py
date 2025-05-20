from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque()
    time = 0
    
    first_truck = truck_weights.pop(0)
    queue.append([first_truck, 0])
    
    time += 1
    
    while queue:
        total_weight = 0
        time += 1
        
        #모든 트럭의 위치 +1
        for t in queue:
            t[1] += 1
        
        #마지막 트럭 도착시 다리에서 내려옴
        if queue[0][1] == bridge_length:
            queue.popleft()
        
        #다리위 모든트럭 무게 합
        for t in queue:
            total_weight += t[0]
        
        #조건 부합시 다음차 다리로
        if len(truck_weights) > 0:
            if len(queue) < bridge_length:
                next_truck = truck_weights.pop(0)
                if total_weight + next_truck <= weight:
                    queue.append([next_truck, 0])
                else:
                    truck_weights.insert(0, next_truck)
        
        
        if len(queue) == 0 and len(truck_weights) != 0:
            first_truck = truck_weights.pop(0)
            queue.append([first_truck, 0])

    return time
            
            
            
            
        