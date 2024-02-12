class Solution(object):
    def majorityElement(self, nums):

        threshold = math.floor(len(nums) / 2)
        for num in set(nums):  
            if nums.count(num) > threshold:
                result=num

        return result
