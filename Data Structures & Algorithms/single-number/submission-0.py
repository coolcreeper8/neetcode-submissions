class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] == nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[i]
