import sys

for line in sys.stdin:
    line = line.strip()
    if line == "DONE":
        break

    cleaned = ''.join(ch.lower() for ch in line if ch.isalpha())

    if cleaned == cleaned[::-1]:
        print("You won't be eaten!")
    else:
        print("Uh oh..")