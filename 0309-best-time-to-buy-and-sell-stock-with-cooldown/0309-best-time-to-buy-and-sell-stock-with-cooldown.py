from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        return self.findMaxProfit(prices, 0, 1, dp)
    
    def findMaxProfit(self, prices, idx, isBuy, dp):
        if idx >= len(prices):
            return 0
        if dp[idx][isBuy] != -1:
            return dp[idx][isBuy]
        if isBuy:
            dp[idx][isBuy] = max(-prices[idx] + self.findMaxProfit(prices, idx + 1, 0, dp), 
                         self.findMaxProfit(prices, idx + 1, 1, dp))
        else:
            dp[idx][isBuy] = max(prices[idx] + self.findMaxProfit(prices, idx + 2, 1, dp), 
                         self.findMaxProfit(prices, idx + 1, 0, dp))
        return dp[idx][isBuy]