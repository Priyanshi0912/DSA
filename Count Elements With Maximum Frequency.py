class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        ans=0
        for ele in nums:
            if ele not in d:
                d[ele]=1
            else:
                d[ele]+=1
        m=max(d.values())
        for val in d.values():
            if val==m:
                ans+=val

        return ans
