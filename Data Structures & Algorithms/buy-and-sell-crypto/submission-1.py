class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for x in range(len(prices) - 1):
            buy = prices[x]
            sell = max(prices[x+1:])
            
            profit = max((sell - buy), profit)
        
        return profit