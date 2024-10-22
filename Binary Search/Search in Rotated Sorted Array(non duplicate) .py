class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target and target<=nums[mid]:#check for left part
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:#check for right part
                    low=mid+1
                else:
                    high=mid-1
        return -1
