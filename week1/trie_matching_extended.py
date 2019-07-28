# python3

import sys

NA = -1


class Node:

    def __init__(self):
        self.next = [NA] * 4
        self.patternEnd = False


def solve(text, n, patterns):
    result = []  #
    trie = []  #
    trie[0] = 0
    letterToIndex = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        }
    for i in range(n):
        current_node = 0
        for j in range(len(patterns[i])):
            current_symbol = int(letterToIndex.get(patterns[i]), -1)
            if trie[current_node].next[current_symbol] != NA:
                current_node = trie[current_node].next[current_symbol]
            else:
                trie.append(len(trie) - 1)
                current_node = len(trie)
			if j == len(patterns[i] - 1):
				trie[current_node].patternEnd = True 

    for i in range(len(text)):
        (current_index, current_node) = (i, 0)
        current_symbol = int(letterToIndex.get(patterns[i]), -1)
        while True:
            if trie[current_node].patternEnd:
                result.append(i)
                break
            elif trie[current_node].next[current_symbol] != NA:
                current_node = trie[current_node].next[current_symbol]
                current_index += 1
                if current_index == len(text):
                    if trie[current_node].patternEnd:
                        result.append(i)
                    break
            else:
                break
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')