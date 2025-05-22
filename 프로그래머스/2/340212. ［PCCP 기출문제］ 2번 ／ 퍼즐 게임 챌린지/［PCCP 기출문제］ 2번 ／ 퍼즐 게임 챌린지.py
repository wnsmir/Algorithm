def check(diffs, times, limit, level):
    time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            time += times[i]
        else:
            mistake = diffs[i] - level
            prev_time = times[i-1] if i > 0 else 0
            time += mistake * (times[i] + prev_time) + times[i]
        if time > limit:
            return False
    return True

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if check(diffs, times, limit, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer