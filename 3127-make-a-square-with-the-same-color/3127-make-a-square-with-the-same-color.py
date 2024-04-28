class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows - 1):
            for y in range(cols - 1):
                w,b=0,0
                if grid[x][y]=='B':
                    b+=1
                else:
                    w+=1
                if grid[x+1][y]=='B':
                    b+=1
                else:
                    w+=1
                if grid[x][y+1]=='B':
                    b+=1
                else:
                    w+=1
                if grid[x+1][y+1]=='B':
                    b+=1
                else:
                    w+=1
                if w>=3 or b>=3:
                    return True
        return False
