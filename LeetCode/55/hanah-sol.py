class Solution:
    # 초간단 풀이
    def canJump(self, nums: List[int]) -> bool:
        p = nums[0]
        for i in range(1, len(nums)):
            if p >= i:
                p = max(p, nums[i] + i)
        return p >= len(nums) - 1

    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i  # 타겟 크기 감소
        return target == 0

    # dp
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n - 1:
                dp[i] = 1  # 점프 가능

            elif i + nums[i] < n - 1:
                # 점프 가능한 구간 내에서
                # 끝까지 도달 가능한 위치가 있는지
                dp[i] = max(dp[i : i + nums[i] + 1])

            elif nums[i] == 0:
                dp[i] = 0

        return dp[0] == 1
