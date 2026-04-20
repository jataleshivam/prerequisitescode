import sys

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

for line in sys.stdin:
    result = ""
    for ch in line.rstrip("\n"):
        if ch == ' ':
            result += ' '
        else:
            result += keyboard[keyboard.index(ch) - 1]
    print(result)