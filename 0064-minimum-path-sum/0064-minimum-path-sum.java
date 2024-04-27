class Solution {
    public int minPathSum(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        int[][] minPaths=new int[m][n];
        minPaths[0][0]=grid[0][0];
        for(int i=1;i<m;i++){
            minPaths[i][0]=minPaths[i-1][0]+grid[i][0];
        }
        for(int j=1;j<n;j++){
            minPaths[0][j]=minPaths[0][j-1]+grid[0][j];
        }
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
            minPaths[i][j]=Math.min(minPaths[i-1][j],minPaths[i][j-1])+grid[i][j];
        }
        }
        return minPaths[m-1][n-1];
    }
}