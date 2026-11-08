import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -1*stone)
        
        # now do simulation
        while len(maxheap) > 1:
            heaviest = -1*heapq.heappop(maxheap)
            second = -1 * heapq.heappop(maxheap)
            if second < heaviest:
                # second is preserved
                heapq.heappush(maxheap, -1 * (heaviest - second))
        if len(maxheap) == 0:
            return 0
        return -1*maxheap[0]