class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=""
        for ele in words:
            if ele==ele[::-1]:
                ans=ele
                break
        return ans
        
