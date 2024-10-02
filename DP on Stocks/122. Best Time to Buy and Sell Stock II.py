class Solution:
    def func(self,prices,ind,canbuy,dp):
        if ind==len(prices): # complete list is exhausted
            return 0
        if dp[ind][canbuy]!=-1:
            return dp[ind][canbuy]
        if canbuy:
            buy= -1*prices[ind]+ self.func(prices,ind+1,0,dp) #buy and set buy starus as 0
            notbuy= 0 + self.func(prices,ind+1,1,dp)  # not buy and set buy status as 1
            dp[ind][canbuy]= max(buy,notbuy)
        else:
            sell = prices[ind]+self.func(prices,ind+1,1,dp) # sell and set buy status as 1
            notsell = 0+ self.func(prices,ind+1,0,dp) #not sell and set buy status as 0
            dp[ind][canbuy]= max(sell,notsell)
        return dp[ind][canbuy]

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*(2) for _ in range(n)]
        return self.func(prices,0,1,dp)
        
