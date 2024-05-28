class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares=[]
        for x in range(1,n+1):
            sqr = x*x
            if sqr <= n:
                perfect_squares.append(sqr)
            else:
                break
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for x in range(2,n+1):
            min_sqrs = n
            for sqr in perfect_squares:
                if sqr <= x:
                   min_sqrs = min(min_sqrs, dp[x-sqr])
            dp[x] = min_sqrs+1
        return dp[n]
         
        