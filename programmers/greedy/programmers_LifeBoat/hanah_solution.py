def solution(people, limit):
    answer = 0
    sorted_p = sorted(people, reverse= True)
    i = -1
    
    # 끝에서 끝으로 투 포인터?를 활용해본다
    while i < len(sorted_p)-2:
        i += 1
        if sorted_p[i] + sorted_p[-1] > limit:
            continue
        sorted_p.pop()

    answer = len(sorted_p)
    return answer