def solution(brown, yellow):
    answer = []
    print(yellow)
    inside = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            j = yellow//i
            if i <= j:
                inside.append((i, j))
                
    
    for a, b in inside:
        print(a,b)
        res = a*2 + b*2 + 4
        if brown == res:
            return [b+2, a+2]
