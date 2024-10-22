class Solution:
    def first(self, nums, target):
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

    def last(self, nums, target):
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

	def count(self,arr, n, x):
	    first=self.first(arr,x) 
	    last=self.last(arr,x)
	    if first==-1:
	        return 0
	    return last-first+1
