class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = ord(s1[i-1]) + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        ascii_s1 = 0
        ascii_s2 = 0
        for i in range(m):
            ascii_s1 += ord(s1[i])
        
        for j in range(n):
            ascii_s2 += ord(s2[j])
        
        return ascii_s1 + ascii_s2 - 2*dp[m][n]      
