class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if ((-1*nums[i]) in nums):
                return (-1)*nums[i]

        return -1
