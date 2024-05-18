class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        return self.findMaxProfit(prices, 0, 1, dp,fee)
    
    def findMaxProfit(self, prices, idx, isBuy, dp,fee):
        if idx == len(prices):
            return 0
        if dp[idx][isBuy] != -1:
            return dp[idx][isBuy]
        
        if isBuy:
            dp[idx][isBuy] = max(-prices[idx] + self.findMaxProfit(prices, idx + 1, 0, dp,fee), 
                         self.findMaxProfit(prices, idx + 1, 1, dp,fee))
        else:
            dp[idx][isBuy] = max(prices[idx]-fee + self.findMaxProfit(prices, idx + 1, 1, dp,fee), 
                         self.findMaxProfit(prices, idx + 1, 0, dp,fee))
        return dp[idx][isBuy]