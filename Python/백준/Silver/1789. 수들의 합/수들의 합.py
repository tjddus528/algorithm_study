s = int(input())

count = 0
value = 0
num = 1
while True:
    value += num
    num += 1
    count += 1
    if s <= value:
        break

if s < value:
    count -= 1
print(count)