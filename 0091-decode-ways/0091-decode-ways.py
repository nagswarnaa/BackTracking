class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0    
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for x in range(2,n+1):
            a=int(s[x-1])
            b=int(s[x-2:x])
            if a!=0:
                dp[x]+=dp[x-1]
            if 10<=b<=26:
                dp[x]+=dp[x-2]
        return dp[n]
            



        