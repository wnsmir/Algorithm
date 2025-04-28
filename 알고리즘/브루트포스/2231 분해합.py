def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
N = int(input())
N <= 1000000
gen = []
for i in range(N):
    if i + sum_of_digits(i) == N:
        gen.append(i)

if len(gen) == 0:
    print(0)
else:
    print(gen[0])