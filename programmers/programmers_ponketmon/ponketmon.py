def solution(nums):
    youcanget = len(nums)//2
    length = len(set(nums))
    if youcanget < length:
        return youcanget
    else:
        return length