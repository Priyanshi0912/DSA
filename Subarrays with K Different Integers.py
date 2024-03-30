from collections import defaultdict
class Solution:
    def atMostK(self, nums, k):
        l, r, count = 0, 0, 0
        d = defaultdict(int)
        distinct_count = 0
        
        while r < len(nums):
            if d[nums[r]] == 0:
                distinct_count += 1
            d[nums[r]] += 1
            
            while distinct_count > k:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    distinct_count -= 1
                l += 1
                
            count += r - l + 1
            r += 1
        
        return count

    def subarraysWithKDistinct(self, nums, k):
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
