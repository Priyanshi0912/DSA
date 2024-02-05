class Solution:
    def firstUniqChar(self, s: str) -> int:
       
        ans=-1
        for i in s:
            if s.count(i)==1:
                ans=s.index(i)
                break
                
        return ans
                
