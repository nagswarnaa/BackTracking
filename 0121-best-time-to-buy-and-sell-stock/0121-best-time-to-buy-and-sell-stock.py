class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price=prices[0]
        profit=0
        for x in prices[1:]:
            cost= x-minimum_price
            profit=max(profit,cost)
            minimum_price=min(x,minimum_price)
        return profit
        