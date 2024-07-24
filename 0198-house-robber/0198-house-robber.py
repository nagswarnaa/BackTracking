class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for x in range(2, n):
            dp[x] = max(dp[x-1], dp[x-2]+nums[x])
        return dp[n-1]
        