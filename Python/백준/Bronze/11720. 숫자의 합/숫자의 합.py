n = int(input())
data = input().rstrip()
nums = []
for d in data:
    nums.append(int(d))
print(sum(nums))