import sys

it = iter(sys.stdin.read().split())
T = int(next(it))
out_lines = []

for _ in range(T):
    x1 = int(next(it)); y1 = int(next(it)); r1 = int(next(it))
    x2 = int(next(it)); y2 = int(next(it)); r2 = int(next(it))

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy          # 중심 거리의 제곱
    rp = r1 + r2
    rm = abs(r1 - r2)
    rp2 = rp * rp
    rm2 = rm * rm

    if d2 == 0 and r1 == r2:
        out_lines.append("-1")          # 같은 원
    elif d2 > rp2:
        out_lines.append("0")           # 서로 멀리
    elif d2 == rp2:
        out_lines.append("1")           # 외접
    elif d2 < rm2:
        out_lines.append("0")           # 내부에서 만나지 않음
    elif d2 == rm2 and d2 != 0:
        out_lines.append("1")           # 내접
    else:
        out_lines.append("2")           # 두 점에서 만남

print("\n".join(out_lines))