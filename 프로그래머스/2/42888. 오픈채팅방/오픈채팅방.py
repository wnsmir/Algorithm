from collections import defaultdict

def solution(record):
    # uid : [현재이름, msg_idx1, msg_idx2, ...]
    users = defaultdict(list)
    answer = []
    
    def change_name(uid, name):
        change_list = users[uid]
        if not change_list:
            return
        # 현재 이름 갱신
        change_list[0] = name
        # 과거 메시지들 닉네임 갱신 (i=1: Enter, i=2: Leave, 번갈아가며)
        for i in range(1, len(change_list)):
            idx = change_list[i]
            if i % 2 == 0:   # 짝수: 나감
                answer[idx] = f"{name}님이 나갔습니다."
            else:            # 홀수: 들어옴
                answer[idx] = f"{name}님이 들어왔습니다."
    
    count = 0
    for i in range(len(record)):
        parts = record[i].split()  # 공백 여러 개 대응
        mode = parts[0]
        uid = parts[1]
        name = parts[2] if len(parts) > 2 else None
        mode_lower = mode.lower()

        if mode_lower == "enter":
            if users[uid]:
                users[uid][0] = name  # 기존 사용자: 이름만 갱신
            else:
                users[uid] = [name]   # 신규: [이름]으로 초기화
            
            # 메시지 추가 및 인덱스 기록
            answer.append(f"{name}님이 들어왔습니다.")
            users[uid].append(count)
            count += 1

            # 과거 메시지 닉네임 모두 최신으로 반영
            change_name(uid, name)

        elif mode_lower == "leave":
            # 현재 저장된 이름으로 메시지 작성 (항상 존재한다고 가정되지만 방어코드 추가)
            if not users[uid]:
                users[uid] = [name or ""]
            curr_name = users[uid][0]

            answer.append(f"{curr_name}님이 나갔습니다.")
            users[uid].append(count)  # Leave 도 인덱스 기록(짝수/홀수 규칙 유지)
            count += 1

        elif mode_lower == "change":
            # 닉네임만 바꾸고 과거 메시지 일괄 갱신
            change_name(uid, name)

    return answer