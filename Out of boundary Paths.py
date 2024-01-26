class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mo=10**9 +7
        dp = [[[-1] * n for _ in range(m)] for _ in range(maxMove + 1)]
        def dfs(k: int,i: int,j:int):
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if k==0:
                return 0
            if dp[k][i][j]!=-1:
                return dp[k][i][j]
            dp[k][i][j]=(dfs(k-1,i+1,j)+dfs(k-1,i-1,j)+dfs(k-1,i,j+1)+dfs(k-1,i,j-1))%mo
            return dp[k][i][j]
        return dfs(maxMove,startRow,startColumn)
