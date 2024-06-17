class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left=0
        right=int(math.sqrt(c))
        
        while(left<=right):
            z=(left*left)+(right*right)
            if (z>c):
                right-=1
            elif (z<c):
                left+=1
            else:
                return True
                
        return False
        
