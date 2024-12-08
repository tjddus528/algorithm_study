a = list(int(i) for i in input())
b = list(int(i) for i in input())

def howlong(ak, bk):
    if ak == 0:
        return bk + max(len(a), len(b) - bk)
    if bk == 0:
        return ak + max(len(b), len(a) - ak)

def match(ak, bk):
    new = []
    for c in zip(a[ak:], b[bk:]):
        if sum(c) >= 4:
            return False
        else:
            new.append(sum(c))
    return True


result = len(a) + len(b)
for ak in range(len(a)):
    if match(ak, 0):
        result = min(result, howlong(ak, 0))
for bk in range(len(b)):
    if match(0, bk):
        result = min(result, howlong(0, bk))
print(result)
