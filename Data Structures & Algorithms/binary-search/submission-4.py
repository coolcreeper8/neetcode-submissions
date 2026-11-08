class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = len(nums) // 2
        lower = 0
        upper = len(nums) - 1
        while lower <=upper:
            if nums[ind] == target:
                return ind
            if nums[ind] > target:
                upper = ind - 1
                ind = (upper + lower) // 2
            else:
                lower = ind + 1
                ind = (upper + lower) // 2
        
        return -1