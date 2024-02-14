class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg=0,1
        ans=nums.copy()
        for i in range(len(nums)):
            if nums[i]>=0:
                ans[pos]=nums[i]
                pos+=2
            else:
                ans[neg]=nums[i]
                neg+=2
        return ans
            
