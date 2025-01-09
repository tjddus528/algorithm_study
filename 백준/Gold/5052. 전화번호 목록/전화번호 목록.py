import sys
input = sys.stdin.readline
def sol():
    for i in range(n - 1):
        if phone[i] == phone[i + 1][:len(phone[i])]: return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    phone = sorted(list(input().rstrip() for _ in range(n)))
    print(sol())