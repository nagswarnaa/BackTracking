class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for x in range(n-2,-1,-1):
            temp=1
            for y in range(x+1,n):
                if nums[y]>nums[x]:
                    temp=max(temp,1+dp[y])
            dp[x]=temp
        return max(dp)

        