def solution(nums):
    mid = len(nums)//2
    kinds = len(set(nums)) 
    if kinds >= mid: 
        return mid
    else:
        return kinds