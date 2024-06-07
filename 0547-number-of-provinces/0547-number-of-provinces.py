class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        no_of_provinces = 0
        for x in range(n):
            if not visited[x]:
                no_of_provinces+=1
                self.dfs(x, visited, n, isConnected)
        return no_of_provinces


    def dfs(self, idx, visited, n, isConnected):
        stk = [idx]
        while len(stk) >= 1:
            idx = stk.pop()
            visited[idx] = True
            for x in range(n):
                if isConnected[idx][x] == 1 and not visited[x]:
                    stk.append(x)

        