class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxp = 0
        while left < len(prices):
            right = left + 1
            while right < len(prices):
                maxp = max(maxp, prices[right] - prices[left])
                right = right + 1
            left = left + 1
        return maxp 
            
