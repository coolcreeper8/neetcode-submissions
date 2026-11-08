class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        right = 0
        maxp = 0
        while right < len(prices):
            minsofar = min(minsofar, prices[right])
            maxp = max(maxp, prices[right] - minsofar)
            right +=1
        return maxp
            
