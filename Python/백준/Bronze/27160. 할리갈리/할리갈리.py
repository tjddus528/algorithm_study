n = int(input())
fruits = {'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}

for _ in range(n):
    f, cnt = input().split()
    fruits[f] += int(cnt)
def check():
    for f in fruits:
        if fruits[f] == 5:
            return True
    return False

if check(): print('YES')
else: print('NO')

