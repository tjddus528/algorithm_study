import sys
input = sys.stdin.readline
n = int(input())

sugars = [5, 3]

count = 0
while n > 0:
    if n % 5 == 0:
        n -= 5
        count += 1
    else:
        n -= 3
        count += 1

    if n < 0:
        count = -1

print(count)
