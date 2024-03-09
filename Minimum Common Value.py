class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s= set(nums1) & set(nums2)
        if ( len(s)>0):
            return min(list(s))
        else:
            return -1
