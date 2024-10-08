class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = '#'
        while stack:
            s[stack[-1]] = '#'
            stack.pop()
        ans = []
        for i in range(len(s)):
            if s[i] != '#':
                ans.append(s[i])
        return "".join(ans)
