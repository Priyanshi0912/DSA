class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #iterative 
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if (nums[mid]==target):
                return mid
            elif (nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return -1




_______________________________________________________

#Recursive
class Solution:
    def func(self,nums,low,high,target):
        
        if (low>high):
            return -1 #base case
        mid=(low+high)//2
        if (nums[mid]==target):
            return mid
        elif nums[mid]<target:
            return self.func(nums,mid+1,high,target)
        return self.func(nums,low,mid-1,target)
    def search(self, nums: List[int], target: int) -> int:
        return self.func(nums,0,len(nums)-1,target)
