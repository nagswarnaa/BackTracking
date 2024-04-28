class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        rows_count=[0]*rows
        cols_count=[0]*cols
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    rows_count[x]+=1
                    cols_count[y]+=1
        total_count=0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    total_count+=(rows_count[x]-1)*(cols_count[y]-1)
        return total_count


                