n = int(input())
for t in range(1, n+1):
    data = list(input().split())
    print(f"Case #{t}:", " ".join(data[::-1]))
