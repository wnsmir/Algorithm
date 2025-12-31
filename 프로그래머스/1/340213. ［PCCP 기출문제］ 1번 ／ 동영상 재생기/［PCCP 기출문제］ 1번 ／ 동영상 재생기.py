def solution(video_len, pos, op_start, op_end, commands):

    m, s = [int(x) for x in pos.split(":")]
    ops_m, ops_s = [int(x) for x in op_start.split(":")]
    ope_m, ope_s = [int(x) for x in op_end.split(":")]
    vl_m, vl_s = [int(x) for x in video_len.split(":")]   # ✅ 추가

    def to_sec(mm, ss):
        return mm * 60 + ss

    def from_sec(sec):
        mm = sec // 60
        ss = sec % 60
        return mm, ss

    # 추가: 영상 길이 범위로 클램프
    def clamp_video(mm, ss):
        cur = to_sec(mm, ss)
        end = to_sec(vl_m, vl_s)
        if cur < 0:
            cur = 0
        if cur > end:
            cur = end
        return from_sec(cur)

    # 기존 오프닝 스킵 로직을 "총초 비교"로만 바꿈
    def skip_opening(mm, ss):
        cur = to_sec(mm, ss)
        ops = to_sec(ops_m, ops_s)
        ope = to_sec(ope_m, ope_s)
        if ops <= cur <= ope:
            return ope_m, ope_s
        return mm, ss

    # 시작 위치 처리: 클램프 후 오프닝 스킵
    m, s = clamp_video(m, s)
    m, s = skip_opening(m, s)
    m, s = clamp_video(m, s)

    for command in commands:

        if command == "next":
            s += 10
            if s >= 60:
                m += 1
                s -= 60

        elif command == "prev":
            if s >= 10:
                s -= 10
            else:
                if m == 0:
                    m, s = 0, 0
                else:
                    s += 50
                    m -= 1

        # 이동 후: 클램프 -> 오프닝 스킵 -> 다시 클램프
        m, s = clamp_video(m, s)
        m, s = skip_opening(m, s)
        m, s = clamp_video(m, s)

    return str(m).zfill(2) + ":" + str(s).zfill(2)