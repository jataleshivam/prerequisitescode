import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for line in sys.stdin:
    n = int(line.strip())
    rev = int(str(n)[::-1])

    if is_prime(n):
        if rev != n and is_prime(rev):
            print(f"{n} is emirp.")
        else:
            print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")