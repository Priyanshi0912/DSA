class Solution:
    def findKRotation(self, nums):
        low=0
        high=len(nums)-1
        ans=float('inf')
        index=0
        while(low<=high):
            mid=(low+high)//2
            if nums[low]<=nums[mid]:  #left part is sorted
                if nums[low]<ans:
                    index=low
                    ans=nums[low]
                
                low=mid+1
            else: #right part is sorted
                if nums[mid]<ans:
                    ans=nums[mid]
                    index=mid
                
                
                high=mid-1
        return index
