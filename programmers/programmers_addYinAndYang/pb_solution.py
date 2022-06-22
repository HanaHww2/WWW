def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        answer = answer + absolute if sign else answer - absolute
    return answer


print(solution([4, 7, 12], [True, False, True]) == 9)
print(solution([1, 2, 3], [False, False, True]) == 0)