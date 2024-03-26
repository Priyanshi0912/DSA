class Solution:
    def swap(self, nums: List[int], i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            ele = nums[i]
            if 1 <= ele <= n and nums[ele - 1] != ele:
                self.swap(nums, ele - 1, i)
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
