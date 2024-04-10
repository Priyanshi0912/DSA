class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        ans=[0]*n
        q = deque(range(len(deck)))
        deck=sorted(deck)
        i=0
        while q:
            ans[q.popleft()]=deck[i]
            i+=1
            if q:
                q.append(q.popleft())
        return ans

            
