class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()


        def twoSum(arr, target):
            hashm = {}
            out = set()
            for i in range(len(arr)):
                if target - arr[i] in hashm:
                    tup = tuple(sorted([target - arr[i], arr[i]]))
                    out.add(tup)
                hashm[arr[i]] = i
            
            return out


        for i in range(len(nums)):
            target = -1 * nums[i]
            tups = twoSum(nums[i+1:], target)

            for tup in tups:
                newtup = tuple(sorted([val for val in tup] + [nums[i]]))
                result.add(newtup)
            
        
        result = list(result)
        for i in range(len(result)):
            result[i] = list(result[i])
        return result