class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans=0
        buy=prices[0]
        for i in range(1,len(prices)):
            ans=max(ans,prices[i]-buy)
            buy=min(buy,prices[i])
        return ans
