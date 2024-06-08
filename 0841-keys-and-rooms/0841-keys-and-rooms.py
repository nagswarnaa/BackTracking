class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        self.dfs(rooms, 0, visited)
        return all(visited)

    def dfs(self, rooms, idx, visited):
        stk = []
        stk.extend(rooms[idx])
        visited[idx] = True
        while len(stk) > 0:
            print(idx)
            idx = stk.pop()
            if not visited[idx]:
                visited[idx] = True
                stk.extend(rooms[idx])
        
        