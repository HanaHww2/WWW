# from collections import defaultdict

# def solution(numbers):
#     answer = 0
    
#     # dafaultdict로 기본값이 0인 1~9까지의 키를 가진 딕셔너리 생성 후,
#     # numbers의 원소를 가진 키값은 += 해준다.
#     # 그 후, 해쉬를 전체 탐색하며 값이 0인 키값을 sum한다.
    
#     num_li = defaultdict(int)
#     for n in numbers:
#         num_li[n] += 1
    
#     for i in range(1, 10):
#         if num_li[i] == 0:
#             answer += i
#     return answer

def solution(numbers):
    answer = 0
    # numbers.sort()
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer

# def solution(numbers):
#     return 45-sum(answer)

solution([1,2,3,4,6,7,8,0]) # 14

