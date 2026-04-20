def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

t = int(input())

for _ in range(t):
    n = int(input())
    count = 0

    while not is_palindrome(n):
        rev = int(str(n)[::-1])
        n += rev
        count += 1

    print(count, n)
