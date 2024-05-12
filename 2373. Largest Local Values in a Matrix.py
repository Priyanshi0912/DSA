class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0]*(n-2) for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                x,y=i+1,j+1
                ans[i][j]=max(grid[x-1][y-1],
                      grid[x-1][y],
                      grid[x-1][y+1],
                      grid[x][y-1],
                      grid[x][y],
                      grid[x][y+1],
                      grid[x+1][y-1],
                      grid[x+1][y],
                      grid[x+1][y+1])
        
        return ans
