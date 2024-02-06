class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            b=''.join(sorted(s))
            if b not in d:
                d[b]=[s]
            else:
                d[b].append(s)
        ans=[]
        for val in d.values():
            ans.append(val)
        return ans
