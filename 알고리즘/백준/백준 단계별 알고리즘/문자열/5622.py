a = input()
sum = 0
for i in a:
    if i == 'A' or i == 'B' or i == 'C':
        sum += 3
    elif i == 'D' or i == 'E' or i == 'F':
        sum += 4
    elif i == 'G' or i == 'H' or i == 'I':
        sum += 5
    elif i == 'J' or i == 'K' or i == 'L':
        sum += 6
    elif i == 'M' or i == 'N' or i == 'O':
        sum += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        sum += 8
    elif i == 'T' or i == 'U' or i == 'V':
        sum += 9
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        sum += 10

print(sum)
