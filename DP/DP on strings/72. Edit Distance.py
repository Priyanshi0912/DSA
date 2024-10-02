class Solution:
    def lcs(self,n,word1,m,word2,ind1,ind2,dp):
        if ind1<0 :
            return ind2+1
        if ind2<0:
            return  ind1+1
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if word1[ind1]==word2[ind2]:
            dp[ind1][ind2]= self.lcs(n,word1,m,word2,ind1-1,ind2-1,dp)
        else:
            dp[ind1][ind2]= 1 + min(self.lcs(n,word1,m,word2,ind1-1,ind2,dp),self.lcs(n,word1,m,word2,ind1,ind2-1,dp),self.lcs(n,word1,m,word2,ind1-1,ind2-1,dp))
        return dp[ind1][ind2]
        
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*m for _ in range(n)]
        return self.lcs(n,word1,m,word2,n-1,m-1,dp)
        
