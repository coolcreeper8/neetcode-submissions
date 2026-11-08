class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                pref[i] = pref[i - 1] * nums[i-1]
        for i in range(len(nums)):
            if i != 0:
                suff[-i - 1] = suff[-i] * nums[-i]
        return [pref[i] * suff[i] for i in range(len(nums))]