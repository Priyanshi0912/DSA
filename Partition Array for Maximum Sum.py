class Solution:
    def f(self,ind:int,k:int ,arr: List[int],dp:List[int]):
        n=len(arr)
        if ind==n:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        
        l=0
        m=float('-inf')
        ans=float('-inf')
        for j in range(ind,min(n,ind+k)):
            l+=1
            m=max(m,arr[j])
            s=l*m + self.f(j+1,k,arr,dp)
            ans=max(ans,s)
        dp[ind]= ans

        return dp[ind]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[-1]*len(arr)
        return self.f(0,k,arr,dp)

        
