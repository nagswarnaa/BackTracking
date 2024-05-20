class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n=len(pairs)
        dp=[1]*n
        list.sort(pairs)
        print(pairs)
        for x in range(n-2,-1,-1):
            temp=1
            for y in range(x+1,n):
                if pairs[x][1]<pairs[y][0]:
                    temp=max(temp,1+dp[y])
            dp[x]=temp
        return max(dp)

            

        