class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:
            return min(matrix[0])
        dp=[[0]*n for _ in range(n)]
        dp[n-1]=matrix[n-1]
        for x in range(n-2,-1,-1):
            dp[x][0]=min(dp[x+1][0],dp[x+1][1])+matrix[x][0]
            dp[x][n-1]=min(dp[x+1][n-1],dp[x+1][n-2])+matrix[x][n-1]
            for y in range(1,n-1):
                dp[x][y]=min(dp[x+1][y-1],dp[x+1][y],dp[x+1][y+1])+matrix[x][y]
        return min(dp[0])

