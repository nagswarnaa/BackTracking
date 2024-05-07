class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=0
        for x in nums:
           total_sum+=x
        if total_sum%2!=0:
            return False
        rows=len(nums)+1
        cols=(total_sum//2)+1
        dp=[[False]*cols for x in range(rows)]
        for x in range(rows):
            dp[x][0]=True
        for x in range(1,cols):
            dp[0][x]=False
        
        for x in range(1,rows):
            for y in range(1,cols):
                take_element = False
                if nums[x-1]<=y:
                    take_element = dp[x-1][y-nums[x-1]]
                dp[x][y]= take_element or dp[x-1][y]
        return dp[rows-1][cols-1]


        