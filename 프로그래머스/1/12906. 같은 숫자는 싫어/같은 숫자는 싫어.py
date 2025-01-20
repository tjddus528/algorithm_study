def solution(arr):
    answer = []
    for a in arr:
        if a in answer[-1:]: continue
        answer.append(a)
    return answer