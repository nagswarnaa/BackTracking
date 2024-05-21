class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n=len(arr)
        dp={}
        max_len=0
        for x in arr:
            diff=x-difference
            if diff in dp:
                dp[x]=dp.get(diff,0)+1
            else:
                dp[x]=1
            max_len=max(max_len,dp[x])
        return max_len