def solution(arr, t):
    answer = 0
    leaves = [0]
    for num in arr:
        tmp = []
        print(leaves)
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == t:
            answer += 1
    return answer
