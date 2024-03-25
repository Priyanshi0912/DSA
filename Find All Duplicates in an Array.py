class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        d={}
        for ele in nums:
            if ele not in d:
                d[ele]=1
            else:
                ans.append(ele)
        return ans
