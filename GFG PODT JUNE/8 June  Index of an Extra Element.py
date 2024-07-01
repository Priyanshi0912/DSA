class Solution:
    def findExtra(self,n,a,b):
        ans=-1
        for i in range(n-1):
            if (a[i]==b[i]):
                continue
            else:
                ans=i
                break
        if ans!=-1 :
            return ans
        else:
            return len(b)
            
