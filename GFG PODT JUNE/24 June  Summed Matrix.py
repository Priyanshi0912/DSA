#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        r=abs(q-(n+1))
        if ( n-r)<=0:
            return 0
        else:
            return (n-r)
