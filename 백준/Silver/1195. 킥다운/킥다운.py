a = list(int(i) for i in input())
b = list(int(i) for i in input())

def howlong(ak, bk):
    if ak == 0:
        return bk + max(len(a), len(b) - bk)
    if bk == 0:
        return ak + max(len(b), len(a) - ak)

def match(ak, bk):
    if bk == 0:
        aa = a[ak:ak+min(len(a)-ak, len(b))]
        bb = b[:len(aa)]
    if ak == 0:
        bb = b[bk:bk+min(len(b)-bk, len(a))]
        aa = a[:len(bb)]
    new = []
    for c in zip(aa, bb):
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