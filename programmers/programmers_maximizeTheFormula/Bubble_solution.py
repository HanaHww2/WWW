# n의 갯수가 최대 100개, 중간중간 연산자가 들어가니 숫자를 최대 50개
# 그러면 50 * 3! 해서 시간복잡도는 300정도로 작으니, 완전탐색으로 풀기 가능!
# 그러나 -숫자 연산이어도 절댓값이 크면 되니 완탐은 안 될 수도 있음. 음수를 없애야하기 때문에

from itertools import permutations as perm
from collections import deque

def solution(expression):
    answer = 0
    # 연산기호 순열(3!개) 리스트로 여러 케이스를 검사하며 answer의 최댓값을 구한다
    for priority in list(perm(['+', '-', '*'], 3)):
        answer = max(answer, abs(calculate(priority, expression)))
    return answer


def calculate(priority, expression):
    # 숫자와 연산자를 분리
    arr = deque()
    num = ''
    for x in expression:
        if x.isdigit():
            num += x
        else:
            arr.append(num)
            num = ''
            arr.append(x)
    arr.append(num)
    # 계산
    for op in priority:
        stack = []
        while len(arr) != 0: # 하나씩 빼면서 우선순위 연산기호를 체크
            temp = arr.popleft()
            if temp == op: # 우선순위인 연산기호이면, 해당 기호의 앞뒤 숫자를 계산한다
                result = str(eval(stack.pop()+op+arr.popleft()))
                stack.append(result)
            else:
                stack.append(temp)
        arr = deque(stack)
    return int(arr.pop())

# solution("100-200*300-500+20") # 60420
solution("50*6-3*2") # 300

