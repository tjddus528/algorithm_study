import sys
input = sys.stdin.readline
dct = []
while True:
    str = input().strip()
    if str == '-': break
    dct.append(str)

puzzle = []
while True:
    str = input().strip()
    if str == '#': break
    puzzle.append(str)

for pz in puzzle:
    candi = []
    for word in dct:
        possible = 1
        for s in word:
            if pz.count(s) < word.count(s):
                possible = 0
                break
        if possible: candi.append(word)

    answer = [set() for _ in range(200001)]
    min_cnt, max_cnt = int(1e9), 0
    for center in pz:
        cnt = 0
        for cd in candi:
            if center in cd: cnt += 1
        answer[cnt].add(center)
        min_cnt = min(min_cnt, cnt)
        max_cnt = max(max_cnt, cnt)

    print(''.join(sorted(list(answer[min_cnt]))), min_cnt, ''.join(sorted(list(answer[max_cnt]))), max_cnt)
