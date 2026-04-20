import sys
from itertools import permutations

labels = ['B', 'G', 'C']

for line in sys.stdin:
    bins = list(map(int, line.split()))
    b = [bins[0:3], bins[3:6], bins[6:9]]

    best_moves = float('inf')
    best_config = ""

    for perm in permutations(range(3)):
        moves = 0
        for i in range(3):
            for j in range(3):
                if j != perm[i]:
                    moves += b[i][j]

        config = ''.join(labels[p] for p in perm)

        if moves < best_moves or (moves == best_moves and config < best_config):
            best_moves = moves
            best_config = config

    print(best_config, best_moves)
