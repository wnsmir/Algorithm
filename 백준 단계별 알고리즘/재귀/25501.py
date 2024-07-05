def recursion(s, l, r):
    if l>=r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
    
def is_palindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for _ in range(T):
    A = input()
    is_palindrome(A)
    print(is_palindrome(A), )