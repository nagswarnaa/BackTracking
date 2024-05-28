class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for tar in range(1,target+1):
            for y in nums:
                if y <= tar:
                    dp[tar]+=(dp[tar-y])
        return dp[target]


        