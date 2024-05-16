class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return nums[0]
        dp=[-1]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for x in range(2,n):
            dp[x]=max(nums[x]+dp[x-2],dp[x-1])
        return dp[n-1]
        