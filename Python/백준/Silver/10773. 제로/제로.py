k = int(input())
nums = [int(input()) for i in range(k)]

result = []
for num in nums:
    if result and num == 0:
        result.pop()
    else:
        result.append(num)

print(sum(result))