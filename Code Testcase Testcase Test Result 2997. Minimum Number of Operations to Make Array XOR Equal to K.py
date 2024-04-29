class Solution:
    def minOperations(self, nums, k):
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        result = 0
        k ^= xor_sum  
        while k > 0:
            result += k & 1
            k >>= 1
        
        return result
