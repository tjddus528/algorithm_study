n = int(input())
s = input()

d = [0] * (n+1)
d[0] = 1
number = int(s[0])
prev = number
for i in range(1, n):

    number = number * 10 + int(s[i])

    if 1 <= number <= 641:
        d[i] = d[i-1]
    else:
        if int(s[i]) == 0:
            temp = 1
            for j in range(i, 0, -1):
                if int(s[j]) == 0:
                    temp = temp * 10
                else:
                    temp = temp * int(s[j])
                    break
            prev = temp
        else:
            prev = int(s[i])
        d[i] = d[i - 1] + 1
        number = prev

print(d[n-1])