import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    ages = list(map(int, sys.stdin.readline().split()))
    count = [0] * 101

    for a in ages:
        count[a] += 1

    result = []
    for i in range(1, 101):
        result.extend([str(i)] * count[i])

    print(" ".join(result))