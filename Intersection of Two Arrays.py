class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=[]
        for i in nums1:
            for j in nums2:
                if ( i==j):
                    num.append(i)
        #b=set(num)
        return list (set(num))
