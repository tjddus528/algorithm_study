from functools import cmp_to_key
n = int(input())
data, strs = {}, []
for _ in range(n):
    cnt, s = 0, input()
    for ss in s:
        if ss.isdigit(): cnt += int(ss)
    data[s] = cnt
    strs.append(s)

def custom_sort(a, b):
    if len(a) < len(b): return 1
    elif len(a) == len(b):
        if data[a] < data[b]: return 1
        elif data[a] == data[b]:
            return dict_comp(a, b)
        else: return -1
    else: return -1

def dict_comp(a, b):
    for aa, bb in zip(a, b):
        if ord(aa) < ord(bb): return 1
        elif ord(aa) == ord(bb): continue
        else: return -1

sorted_data = sorted(strs, key=cmp_to_key(custom_sort), reverse=True)
for res in sorted_data: print(res)
