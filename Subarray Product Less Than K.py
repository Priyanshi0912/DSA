class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        product=1
        i,j=0,0
        while(j<n):
            product*=nums[j]
            while (product>=k) and i<=j:
                product/=nums[i]
                i+=1
            count+=(j-i+1)
            j+=1
        return count
