class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)

        # make dp table 
        dp=[[-1]*(m+1) for _ in range(n+1)]
        #fill first row with 0
        for i in range(n+1):
            dp[i][0]=0
        #fill first col with 0
        for j in range(m+1):
            dp[0][j]=0
        #fill rest of the DP
        for row in range(1,n+1):
            for col in range(1,m+1):
                if str1[row-1]==str2[col-1]:
                    dp[row][col]=1+dp[row-1][col-1]
                else:
                    dp[row][col]=max(dp[row-1][col],dp[row][col-1])
        row=n
        col=m
        ans=""
        while(row>0 and col>0):
            if str1[row-1]==str2[col-1]: #same ho gya toh
                ans+=str1[row-1]
                row-=1
                col-=1
            elif dp[row-1][col]>dp[row][col-1]: # left side wala
                ans+=str1[row-1]
                row-=1
            else:
                ans+=str2[col-1]  #select upper wala
                col-=1
        while(row>0):
            ans+=str1[row-1]
            row-=1
        while(col>0):
            ans+=str2[col-1]
            col-=1

        return ans[::-1]


            

        
