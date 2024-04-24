class Solution:
    def f(self,n:int,dp:List[int ]):
        if n==0:
            dp[n]=0
        if n==2 or n==1:
            dp[n]=1
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.f(n-1,dp)+self.f(n-2,dp)+self.f(n-3,dp)
        return dp[n]
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.f(n,dp)
