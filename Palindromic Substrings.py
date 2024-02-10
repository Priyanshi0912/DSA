class Solution:
    def check(self, s: str, i: int, j: int) -> int:
        ans = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            ans += 1
            i -= 1
            j += 1
        return ans

    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.check(s, i, i)
            ans += self.check(s, i, i + 1)
        return ans
        
