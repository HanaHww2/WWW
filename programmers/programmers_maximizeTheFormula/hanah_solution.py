# eval() 을 사용하는 것은 실무에서는 보안상 권장되지 않는다고 한다.
# 문자열을 실행하는 eval() 함수를 사용하는 만큼,
# 문자열을 쪼개는 방식에서 아쉬운 점은
# split() 함수를 미처 바로 생각해내지 못했다는 것이다.

def makeArray(expression):
    exArr = []
    operators = set()
    latest = 0

    for i, e in enumerate(expression):
        if e in ('*', "+", '-'):
            exArr.append(expression[latest:i])
            exArr.append(e)
            operators.add(e)
            latest = i+1
    exArr.append(expression[latest:])

    return exArr, list(operators)


priorities = []


def makePermutation(num_list, temp):
    global priorities

    if len(num_list) < 1:
        priorities.append(temp)
        return

    for i, a in enumerate(num_list):
        temp.append(a)
        makePermutation(num_list[:i]+num_list[i+1:], temp[:])
        temp.pop()


def makeResultByPriority(exArr, operators, priority):
    for j in priority:
        idx = 1
        while idx <= len(exArr)-1:
            if exArr[idx] == operators[j]:
                result = eval(f"{exArr[idx-1]}{exArr[idx]}{exArr[idx+1]}")
                exArr = exArr[:idx-1] + [result] + exArr[idx+2:]
            else:
                idx += 2

    return exArr[0]


def solution(expression):
    answer = 0

    exArr, operators = makeArray(expression)
    makePermutation(list(range(len(operators))), [])

    max_result = 0
    for p in priorities:
        result = makeResultByPriority(exArr, operators, p)
        max_result = max(abs(result), max_result)

    return max_result
