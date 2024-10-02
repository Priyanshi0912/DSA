class Solution:
    def func(self,prices,ind,canbuy,cap,dp):
        if cap==0:
            return 0
        if ind==len(prices): # complete list is exhausted
            return 0
        if dp[ind][canbuy][cap]!=-1:
            return dp[ind][canbuy][cap]
        if canbuy:
            buy= -1*prices[ind]+ self.func(prices,ind+1,0,cap,dp) #buy and set buy starus as 0
            notbuy= 0 + self.func(prices,ind+1,1,cap,dp)  # not buy and set buy status as 1
            dp[ind][canbuy][cap]= max(buy,notbuy)
        else:
            sell = prices[ind]+self.func(prices,ind+1,1,cap-1,dp) # sell and set buy status as 1
            notsell = 0+ self.func(prices,ind+1,0,cap,dp) #not sell and set buy status as 0
            dp[ind][canbuy][cap]= max(sell,notsell)
        return dp[ind][canbuy][cap]

    def maxProfit(self,  k: int,prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*(k+1) for _ in range(2)] for z in range(n)]
        return self.func(prices,0,1,k,dp)
        
