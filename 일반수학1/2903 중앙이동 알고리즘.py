def count_points_after_iterations(N):
    return (2**N + 1)**2

N = int(input())
points = count_points_after_iterations(N)
print(points)