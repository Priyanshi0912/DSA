
#using lower bound , upper bound logic
class Solution:
    def lowerbound(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upperbound(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        if ans == -1:
            return len(nums) - 1  # Return the last index if target is found till the end
        else:
            return ans - 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.lowerbound(nums, target)
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]  # Target not found
        
        upper = self.upperbound(nums, target)
        
        return [lower, upper]



_________________________________________________________


#using binary search

class Solution:
    def first(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        first=-1
        while(low<=high):
            mid=(low+high)//2
            if (nums[mid]==target):
                first= mid
                high=mid-1
            elif (nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return first

    def last(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        last=-1
        while(low<=high):
            mid=(low+high)//2
            if (nums[mid]==target):
                last= mid
                low=mid+1
            elif (nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return last
    




    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums,target), self.last(nums,target)]

        


