class Solution(object):
    def minFallingPathSum(self, grid):
        N=len(grid)
        dp=grid[0]
        for row in range(1,N):
            nextdp=[float('inf')]*N
            for curr_col in range(N):
                for prev_col in range(N):
                    if prev_col!=curr_col:
                        nextdp[curr_col]=min(nextdp[curr_col],
                        grid[row][curr_col]+dp[prev_col])
            dp=nextdp
        return min(dp)
