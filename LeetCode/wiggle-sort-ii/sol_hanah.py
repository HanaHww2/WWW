class Solution:
    def wiggle_replace(self, nums: List[int]):
        temp = []
        length = math.ceil(len(nums)/2)
        small = nums[:length]
        large = nums[length:]

        for _ in range(length):
            if small != []:
                temp.append(small.pop())
            if large != []:
                temp.append(large.pop())
        return temp

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[:] = self.wiggle_replace(nums)

# Slice Assignment/Replacement 에 대해 알게 되었다.
# https://blog.naver.com/PostView.nhn?blogId=youndok&logNo=222285888913
