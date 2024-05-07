class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for x in range(1,amount+1):
            for y in coins:
                diff=x-y
                if diff>=0:
                    dp[x]=min(dp[x],1+dp[diff])
        return dp[amount] if dp[amount]!=amount+1 else -1

        