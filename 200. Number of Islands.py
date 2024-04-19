class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        
        def dfs(grid,i:int,j:int):
            if (i<0 or j<0 or i==n or j==m or grid[i][j]=="0" ):
                return
            grid[i][j]="0"
            dfs(grid,i,j+1)
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
        
        for row in range(n):
            for col in range(m):
                if grid[row][col]=="1":
                    
                    ans+=1
                    dfs(grid,row,col)

        return ans
