class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        noOfPrices=len(prices)
        noOfTrns=0
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(noOfPrices)]
        return self.findProfit(prices,0, 1, noOfPrices,dp,noOfTrns)

    def findProfit(self,prices, idx, isBuy, noOfPrices,dp,noOfTrns):
        if idx==noOfPrices:
            return 0
        if noOfTrns<=2:
            if dp[idx][isBuy][noOfTrns]!=-1:
                return dp[idx][isBuy][noOfTrns]
            if isBuy:
                profit=max(-prices[idx]+self.findProfit(prices, idx+1, 0, noOfPrices,dp,noOfTrns+1),self.findProfit(prices, idx+1, 1, noOfPrices,dp,noOfTrns))
            else:
                profit=max(prices[idx]+self.findProfit(prices, idx+1, 1, noOfPrices,dp,noOfTrns),self.findProfit(prices, idx+1, 0, noOfPrices,dp,noOfTrns))
        else:
            return 0
        dp[idx][isBuy][noOfTrns]=profit
        return dp[idx][isBuy][noOfTrns]

        