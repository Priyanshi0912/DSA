class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for ele in range(len(nums)+1):
            if ele not in nums:
                return ele
        #return -1
