n = int(input())

def is666(num):
    s = str(num)
    for i in range(len(s)-2):
        if s[i] + s[i+1] + s[i+2] == '666':
            return True
    return False

count = 0
number = 666
while True:
    if is666(number):
        count += 1
    if count == n:
        print(number)
        break
    number += 1
