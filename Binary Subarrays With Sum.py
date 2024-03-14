class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsum=c=0
        d=dict()
        d[0]=1 
        for i in nums:
            prefixsum+=i
            if prefixsum-goal in d:
                c+=d[prefixsum-goal]
            if prefixsum in d:
                d[prefixsum]+=1
            else:
                d[prefixsum]=1
        return c
