import sys
input = sys.stdin.readline

a, b = map(int, input().split())

answer = -1
def calc(a, b, step):
    global answer
    if a > b:
        return
    elif a == b:
        answer = step
        return
    else:
        calc(2*a, b, step + 1)
        calc(a*10+1, b, step+1)


calc(a, b, 1)
print(answer)