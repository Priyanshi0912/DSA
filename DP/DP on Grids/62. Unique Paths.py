class Solution:
    def func(self,row,col,m,n,dp):
        if row==(m-1) and col==(n-1):
            return 1
        
        if (row>=m or col>=n):
            return 0

        if dp[row][col]!=-1:
            return dp[row][col]

        down=self.func(row+1,col,m,n,dp)   
        right=self.func(row,col+1,m,n,dp)
        dp[row][col]= down+right
        return dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for _ in range(m+1)]
        return self.func(0,0,m,n,dp)


