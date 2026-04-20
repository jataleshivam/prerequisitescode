import sys

while True:
    try:
        a = input()
        b = input()
    except EOFError:
        break

    freq1 = [0]*26
    freq2 = [0]*26

    for ch in a:
        freq1[ord(ch)-97] += 1
    for ch in b:
        freq2[ord(ch)-97] += 1

    result = ""
    for i in range(26):
        result += chr(i+97) * min(freq1[i], freq2[i])

    print(result)