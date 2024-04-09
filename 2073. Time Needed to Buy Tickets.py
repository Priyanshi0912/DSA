class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        curr=0
        n=len(tickets)
        
        while(tickets[k]!=0):
            if curr==n:
                curr=0
            if tickets[curr]!=0:
                count+=1
                tickets[curr]-=1
            curr+=1
        return count
            
