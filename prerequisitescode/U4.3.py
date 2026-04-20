while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr = [int(input()) for _ in range(n)]

    def key(x):
        return (x % m, x % 2 == 0, x if x % 2 == 1 else -x)

    arr.sort(key=key)

    print(n, m)
    for x in arr:
        print(x)
