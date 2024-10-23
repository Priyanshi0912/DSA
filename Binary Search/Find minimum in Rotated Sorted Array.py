class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if nums[low]<=nums[mid]:  #left part is sorted
                ans=min(ans,nums[low])
                low=mid+1
            else: #right part is sorted
                ans=min(ans,nums[mid])
                high=mid-1
        return ans
            
        