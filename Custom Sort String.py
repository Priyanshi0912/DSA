class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d=dict()
        ans=""
        for ele in s:
            if ele not in d:
                d[ele]=1
            else:
                d[ele]+=1
        
        for ele in order:
            if ele in s:
                ans+=ele*d[ele]
                del d[ele]
        
        for key ,val in d.items():
            ans+=key*val

        return ans
