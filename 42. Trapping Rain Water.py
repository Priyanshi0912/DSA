class Solution:
    def trap(self, height: List[int]) -> int:
        left =[]
        right=[]
        ans=0
        left_max=float('-inf')
        right_max=float('-inf')
        for i in height:
            left_max=max(left_max,i) 
            left.append(left_max) 
        
        print(left)
        for i in height[::-1]:
            right_max=max(right_max,i) 
            right.append(right_max)
        right=right[::-1]
        print(right)
        for i in range(len(height)):
            ans+=(min(right[i],left[i])-height[i])
        return ans
