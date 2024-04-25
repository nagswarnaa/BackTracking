class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n        
        dp=[-1]*n
        dp[0]=1
        dp[1]=2
        for x in range(2,n):
            dp[x]=dp[x-1]+dp[x-2]
        return dp[n-1]
