class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]>x:
                max_profit+=(prices[i]-x)
                x=prices[i]
            else:
                x=min(x,prices[i])
        return max_profit