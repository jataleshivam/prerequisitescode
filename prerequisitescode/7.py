import sys

mapping = {
    **dict.fromkeys("BFPV", '1'),
    **dict.fromkeys("CGJKQSXZ", '2'),
    **dict.fromkeys("DT", '3'),
    'L': '4',
    **dict.fromkeys("MN", '5'),
    'R': '6'
}

for line in sys.stdin:
    prev = ''
    result = ""

    for ch in line.strip():
        code = mapping.get(ch, '')
        if code != prev:
            result += code
        if code != '':
            prev = code
        else:
            prev = ''

    print(result)