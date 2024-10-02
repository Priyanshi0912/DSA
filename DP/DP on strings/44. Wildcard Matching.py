class Solution:
    def allStars(self, p, i):
        # Check if all characters in p from 0 to i are '*'
        for k in range(i + 1):
            if p[k] != "*":
                return False
        return True

    def func(self, s, p, ind1, ind2,dp):
        # If both strings are fully matched
        if ind1 < 0 and ind2 < 0:
            return True
        # If the pattern is exhausted but the string is not
        if ind1 < 0 and ind2 >= 0:
            return False
        # If the string is exhausted but the pattern still has stars to match
        if ind2 < 0 and ind1 >= 0:
            return self.allStars(p, ind1)
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        # Matching character or a '?'
        if p[ind1] == s[ind2] or p[ind1] == "?":
            dp[ind1][ind2]= self.func(s, p, ind1 - 1, ind2 - 1,dp)
        # Handling the '*' in pattern
        elif p[ind1] == "*":
            dp[ind1][ind2]= self.func(s, p, ind1 - 1, ind2,dp) or self.func(s, p, ind1, ind2 - 1,dp)
        else:
            dp[ind1][ind2]= False
        return dp[ind1][ind2]

    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        dp=[[-1]*(m) for _ in range(n)]
        return self.func(s, p, n - 1, m - 1,dp)
