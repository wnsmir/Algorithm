from collections import defaultdict

def solution(fees, records):
    def time_to_min(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    car_list = defaultdict(list)
    for record in records:
        t, num, io = record.split()
        car_list[num].append((t, io))

    total_times = dict()

    for car in car_list:
        times = car_list[car][:]
        #마지막이 들어온거라면 23:59에 나간거로 간주
        if times[-1][1] == "IN":
            times.append(("23:59", "OUT"))
        total = 0
        while times:
            in_time, _ = times.pop(0)
            out_time, _ = times.pop(0)
            in_min = time_to_min(in_time)
            out_min = time_to_min(out_time)
            total += out_min - in_min
        total_times[car] = total

    #요금 계산
    result = []
    base_time, base_fee, unit_time, unit_fee = fees
    for car in sorted(total_times):
        total_time = total_times[car]
        if total_time <= base_time:
            result.append(base_fee)
        else:
            extra = total_time - base_time
            units = (extra + unit_time - 1) // unit_time
            result.append(base_fee + units * unit_fee)
    return result                    