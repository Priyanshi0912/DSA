class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i,n in enumerate(nums):
            if (target-n) in d:
                return [d[target-n],i]
            d[nums[i]]=i
        return
        
