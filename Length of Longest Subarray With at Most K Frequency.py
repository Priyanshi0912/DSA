class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i,j=0,0
        n=len(nums)
        d={}
        ans=1
        while(i<n and j<n ):
            d[nums[j]] = d.get(nums[j], 0) + 1
            if (d[nums[j]]>k):
                ans=max(ans,j-i)
                while d[nums[j]]>k:
                    d[nums[i]]-=1
                    i+=1
            
            j+=1
        return max(ans,j-i)
