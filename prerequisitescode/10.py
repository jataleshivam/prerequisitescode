import sys

for line in sys.stdin:
    words = line.rstrip('\n').split(' ')
    result = ' '.join(word[::-1] for word in words)
    print(result)