def solution(numbers, target):

    length = len(numbers)

    def target_if_zero(target):
        if target == 0:
            return 1
        else:
            return 0

    def dfs(target, n):

        if n == length:
            return target_if_zero(target)

        return dfs(target-numbers[n], n+1) + dfs(target+numbers[n], n+1)

    return dfs(target, 0)
