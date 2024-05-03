class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*n
        if n==1:
            return 0 if s[0]=='0' else 1
        if s[0]=='0':
            return 0
        dp[0]=1
        dp[1]=1 if s[1]=='0' else 2
        for x in range(2,n):
            a=int(s[x])
            b=int(s[x-1:x+1])
            print(b)
            if a!=0:
                dp[x]=dp[x]+dp[x-1]
            if 10<=b<=26:
                dp[x]=dp[x]+dp[x-2]
        return dp[n-1]
            



        