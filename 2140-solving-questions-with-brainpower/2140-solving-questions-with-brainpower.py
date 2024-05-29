class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n= len(questions)
        dp=[-1]*n
        return self.find_maxpoints(0,dp,questions,n)
    def find_maxpoints(self,idx,dp,questions,n):
        if idx >= n:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        dp[idx] = max(questions[idx][0]+self.find_maxpoints(idx+questions[idx][1]+1,dp,questions,n),self.find_maxpoints(idx+1,dp,questions,n))
        return dp[idx]

