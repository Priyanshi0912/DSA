class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mini,maxi,ind=-1,-1,-1
        ans=0
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                ind=i
            if nums[i]==minK:
                mini=i
            if nums[i]==maxK:
                maxi=i
            ans+=max(0,min(maxi,mini)-ind)        
        return ans
