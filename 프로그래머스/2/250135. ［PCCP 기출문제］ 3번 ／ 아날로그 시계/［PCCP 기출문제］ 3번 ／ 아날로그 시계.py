def solution(h1, m1, s1, h2, m2, s2):
    # 1) 구간을 초 단위로 변환
    start = h1 * 3600 + m1 * 60 + s1
    end   = h2 * 3600 + m2 * 60 + s2

    # 2) 충돌 주기를 분수로 표현
    #    초침⇄분침: T_sm = 3600/59  (k번 충돌 시 t = k * (3600/59))
    num_sm, den_sm = 59, 3600
    #    초침⇄시침: T_sh = 43200/719 (k번 충돌 시 t = k * (43200/719))
    num_sh, den_sh = 719, 43200
    #    중복 충돌 주기(초침⇄분침 & 초침⇄시침 동시): 12시간 = 43200초
    L = 43200

    # 3) start~end 구간 내 충돌 횟수 계산 (정수 수식으로 ceil/floor 구현)
    #   * k_sm_start = 최소 k such that k*(3600/59) >= start
    #   * k_sm_end   = 최대 k such that k*(3600/59) <= end
    k_sm_start = (start * num_sm + den_sm - 1) // den_sm
    k_sm_end   = (end   * num_sm) // den_sm
    count_sm   = max(0, k_sm_end - k_sm_start + 1)

    k_sh_start = (start * num_sh + den_sh - 1) // den_sh
    k_sh_end   = (end   * num_sh) // den_sh
    count_sh   = max(0, k_sh_end - k_sh_start + 1)

    # 4) 같은 시점에 두 충돌이 일어나는 (중복) 횟수
    dup_start = (start + L - 1) // L
    dup_end   = end // L
    dup_count = max(0, dup_end - dup_start + 1)

    # 5) 최종 = (초분 충돌 + 초시 충돌) − 중복 충돌
    return count_sm + count_sh - dup_count