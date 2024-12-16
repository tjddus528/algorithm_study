import sys
data = sys.stdin.readline().rstrip()

# - 부호를 기준으로 숫자를 묶어서 저장
plusnumbers = data.split('-')

# 각 숫자 묶음의 합을 구한다
numbers = []
for plus in plusnumbers:
    numbers.append(sum(map(int, plus.split('+'))))

sum = numbers[0]
for number in numbers[1:]:
    sum -= number

print(sum)
