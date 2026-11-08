class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            if num not in freqmap:
                freqmap[num] = 1
            else:
                freqmap[num] += 1
        
        buckets = [[] for a in range(len(nums) + 1)]

        for num, freq in freqmap.items():
            buckets[freq].append(num)
        
        topK = []
        for i in range(len(buckets)):
            for num in buckets[len(buckets) - 1 -i]:
                topK.append(num)
                if len(topK) == k:
                    return topK
        