class Solution:
    max_result = -30000
    min_result = 30000

    # 최대합 찾기
    def find_max_sum(self, temp_sum, current, k):

        if (temp_sum + current > current):
            temp_sum += current
        else:
            temp_sum = current

        self.max_result = max(self.max_result, temp_sum)

        return temp_sum

    # 최솟값 찾기
    def find_min_sum(self, temp_sum, current, k):

        if (temp_sum + current < current):
            temp_sum += current
        else:
            temp_sum = current

        self.min_result = min(self.min_result, temp_sum)

        return temp_sum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        length = len(nums)

        max_temp = 0
        min_temp = 0

        for i in range(length):

            # 최대합 찾기
            max_temp = self.find_max_sum(max_temp, nums[i], i)

            # 최소합 찾기
            min_temp = self.find_min_sum(min_temp, nums[i], i)

        return max(self.max_result, sum(nums) - self.min_result if sum(nums) != self.min_result else self.max_result)

# 다른 방식의 풀이는 없는걸까?
# 암만 생각해봐도 없는 것 같다...흠
