class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        left = 0
        right = len(numbers) - 1

        while left <= right:
            val1 = numbers[left]
            val2 = numbers[right]

            if val1 + val2 == target:
                return [left + 1, right + 1]
            
            if target - val1 in hashmap:
                smallest = min(hashmap[target - val1] + 1, left + 1)
                biggest = max(hashmap[target - val1] + 1, left + 1)
                return [smallest, biggest]
            
            if target - val2 in hashmap:
                smallest = min(right + 1, hashmap[target - val2] + 1)
                biggest = max(right + 1, hashmap[target - val2] + 1)
                return [smallest, biggest]
            
            hashmap[val1] = left
            hashmap[val2] = right
            left+=1
            right-=1