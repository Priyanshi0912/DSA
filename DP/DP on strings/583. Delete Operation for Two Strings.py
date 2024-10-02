class Solution:
    def lcs(self,word1,word2):
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0]=0
        for j in range(m):
            dp[0][j]=0
        ans=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
                ans=max(ans,dp[i][j])
        return ans

    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        return m-self.lcs(word1,word2)



        
