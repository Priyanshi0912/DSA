class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        left,right=0,len(tokens)-1
        ans=0
        tokens.sort()

        while left<=right:
            if power >=tokens[left]:
                ans+=1
                power-=tokens[left]
                left+=1
            elif left<right and ans>0:
                ans-=1
                power+=tokens[right]   
                right-=1
            else:
                return ans        
        return ans
