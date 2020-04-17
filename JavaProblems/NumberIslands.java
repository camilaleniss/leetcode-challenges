package JavaProblems;

public class NumberIslands{

    public static int numIslands(char[][] grid){
        if (grid == null || grid.length==0){
            return 0;
        }

        int numberOfIslands=0; 

        for (int i=0; i<grid.length; i++){
            for (int j=0; j<grid[i].length; j++){
                if (grid[i][j] == '1')
                    numberOfIslands += bfs(grid, i, j);
            }
        }

        return numberOfIslands;
    }

    public static int bfs(char[][] grid, int i, int j){
        if ( i<0 || i>=grid.length || j<0 || j>=grid[i].length || grid[i][j]=='0'){
            return 0;
        }
            
        grid[i][j] = '0';
        bfs(grid, i+1, j);
        bfs(grid, i-1, j);
        bfs(grid, i, j+1);
        bfs(grid, i, j-1);
        return 1;
    }

    public static void main(String [] args){
       char [][] matrix = {{'1','1','0'},{'0','1','0'},{'0','0','1'}};
       char [][] nums = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
       System.out.print("Number of islands: "+numIslands(nums));
    }

}