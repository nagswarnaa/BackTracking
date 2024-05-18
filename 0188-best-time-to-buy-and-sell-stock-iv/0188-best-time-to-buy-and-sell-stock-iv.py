class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        noOfPrices=len(prices)
        noOfTrns=0
        dp = [[[-1] * (k+1) for _ in range(2)] for _ in range(noOfPrices)]
        return self.findProfit(prices,0, 1, noOfPrices,dp,noOfTrns,k)

    def findProfit(self,prices, idx, isBuy, noOfPrices,dp,noOfTrns,k):
        if idx==noOfPrices or noOfTrns>k:
            return 0
        if dp[idx][isBuy][noOfTrns]!=-1:
            return dp[idx][isBuy][noOfTrns]
        if isBuy:
            profit=max(-prices[idx]+self.findProfit(prices, idx+1, 0, noOfPrices,dp,noOfTrns+1,k),self.findProfit(prices, idx+1, 1, noOfPrices,dp,noOfTrns,k))
        else:
            profit=max(prices[idx]+self.findProfit(prices, idx+1, 1, noOfPrices,dp,noOfTrns,k),self.findProfit(prices, idx+1, 0, noOfPrices,dp,noOfTrns,k))
        dp[idx][isBuy][noOfTrns]=profit
        return dp[idx][isBuy][noOfTrns]

        