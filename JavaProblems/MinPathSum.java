package JavaProblems;

public class MinPathSum {

    public static int minPathSum(int[][] grid) {
        if (grid == null){
            return 0;
        }

        return dfs(grid, 0, 0);
    }

    public static int dfs(int[][] grid, int i, int j){
        if (i==grid.length-1 && j==grid[0].length-1)
            return grid[i][j];

        if(i<grid.length-1 && j<grid[0].length-1){
            int r1 = grid[i][j] + dfs(grid, i+1, j);
            int r2 = grid[i][j] + dfs(grid, i, j+1);
            return Math.min(r1,r2);
        }
         
        if(i<grid.length-1){
            return grid[i][j] + dfs(grid, i+1, j);
        }
         
        if(j<grid[0].length-1){
            return grid[i][j] + dfs(grid, i, j+1);
        }

        return 1;
    }

    public int minPathSumDynamic(int[][] grid) {
        if(grid == null || grid.length==0)
            return 0;
     
        int x_length = grid.length;
        int y_length = grid[0].length;
     
        int[][] min_path = new int[x_length][y_length];
        min_path[0][0] = grid[0][0];    
     
        // First row fill cause it will no be edited 
        for(int i=1; i<y_length; i++){
            min_path[0][i] = min_path[0][i-1] + grid[0][i];
        }
     
        // Left row fill cause it will not be edited 
        for(int j=1; j<x_length; j++){
            min_path[j][0] = min_path[j-1][0] + grid[j][0];
        }
     
        for(int i=1; i<x_length; i++){
            for(int j=1; j<y_length; j++){
                if(min_path[i-1][j] > min_path[i][j-1]){
                    min_path[i][j] = min_path[i][j-1] + grid[i][j];
                }else{
                    min_path[i][j] = min_path[i-1][j] + grid[i][j];
                }
            }
        }
     
        return min_path[x_length-1][y_length-1];
    }

    public static void main(String [] args){
        int[][] grid = {{1,3,1},{1,5,1},{4,2,1}};
        System.out.println("The minimun path is: "+minPathSum(grid));
    }
}