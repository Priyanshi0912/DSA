class Solution:
    def func(self,s,t,ind1,ind2,dp):
        if (ind2<0):
            return 1
        if (ind1<0):
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if s[ind1]==t[ind2]:
            dp[ind1][ind2]= self.func(s,t,ind1-1,ind2-1,dp)+ self.func(s,t,ind1-1,ind2,dp)
        else:
            dp[ind1][ind2]= self.func(s,t,ind1-1,ind2,dp)
        return dp[ind1][ind2]
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*(m) for _ in range(n)]
        return self.func(s,t,n-1,m-1,dp)

        
