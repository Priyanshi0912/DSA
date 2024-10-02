class Solution:
    def all_longest_common_subsequences(self, s, t):
        n = len(s)
        m = len(t)
        
        # Initialize DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Length of the LCS
        l = dp[n][m]
        
        # Construct the LCS string by backtracking
        i, j = n, m
        ans = [""] * l  # Initialize a list to store LCS characters
        
        index = l - 1  # Start from the last position in the LCS string
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                ans[index] = s[i - 1]  # Include character in LCS
                index -= 1
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1  # Move upwards in the DP table
            else:
                j -= 1  # Move left in the DP table
        
        return ''.join(ans)
