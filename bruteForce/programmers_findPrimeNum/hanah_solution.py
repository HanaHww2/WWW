import math
from collections import deque


def solution(numbers):
    answer = 0
    num_list = set()

    def dfs(prev, nums):
        # 없어도 되는 탈출 조건
        # (nums 길이가 0이면 아래 for문이 동작하지 않으므로)
        # 이지만, 그래도 기분상 넣는다.
        if len(nums) == 0:
            return
        for i in range(len(nums)):

            if prev and prev[0] == '0':
                continue

            temp = prev + nums[i]
            if int(temp) in num_list:
                continue
            num_list.add(int(temp))

            dfs(temp, nums[:i]+nums[i+1:])

    def chk_prime_num(num):
        for n in range(2, int(num**(1/2))+1):
            if num % n == 0:
                return False
        return True

    dfs('', numbers)
    for n in num_list-{0, 1}:
        if chk_prime_num(n):
            answer += 1

    return answer


# 과거 풀이
answer = 0
checked = []


def solution(numbers):
    s = ''
    dfs(numbers, s)
    return answer


def dfs(nums, s):
    global answer

    if not nums:
        return 0

    for i in range(0, len(nums)):
        if s == '' and nums[i] == '0':
            continue
        s += nums[i]
        num = int(s)
        if num not in checked:
            answer += check_prime(num)
        dfs(nums[:i]+nums[i+1:], s)
        s = s[:-1]


def check_prime(n):
    checked.append(n)
    if n < 2:
        return 0
    for div in range(2, math.floor(n/2)+1):  # math.ceil(s/2) 는 2의 배수에서 문제 발생
        if n % div == 0:
            return 0
    return 1
