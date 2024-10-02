class Solution:
    def lps(self,s):
        return self.lcs(s,s[::-1])
    def lcs(self,s1,s2):
        n=len(s1)
        m=len(s2)
        dp=[[0]*(m+1) for _ in range((n+1))]
        for row in range(1,n+1):
            for col in range(1,m+1):
                if s1[row-1]==s2[col-1]:
                    dp[row][col]= 1+ dp[row-1][col-1]
                else:
                    dp[row][col]= max(dp[row-1][col],dp[row][col-1])
        return dp[n][m]
        
    def minInsertions(self, s: str) -> int:
        return len(s)-self.lps(s)
