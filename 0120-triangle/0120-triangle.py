class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows=len(triangle)
        dp=[[-1] * len(row) for row in triangle]
        temp_row=[]
        for x in range(len(triangle[rows-1])):
            dp[rows-1][x]=triangle[rows-1][x]

        for x in range(rows-2,-1,-1):
            for y in range(len(triangle[x])):
                dp[x][y]=min(dp[x+1][y]+triangle[x][y],dp[x+1][y+1]+triangle[x][y])
        return dp[0][0]