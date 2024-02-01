class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums),3):
            arr=nums[i:i+3]
            if (max(arr)-min(arr))<=k:
                ans.append(arr)
            else:
                ans=[]
                break
        return ans
        
