class Solution:
    def swap(self,arr,i,j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    def findPartition(self,arr,low,high):
        pivot= arr[low]
        i=low
        j=high
        while(i<j):
            #next element who is greater than pivot element
            while(pivot>=arr[i] and i<=high-1):
                i+=1
            #next element who is smaller than pivot element
            while(pivot<arr[j] and j>=low +1 ):
                j-=1

            if (i<j):
                self.swap(arr,i,j)
        self.swap(arr,low,j)
        return j
    def quickSort(self, arr, low, high):
        if (low<high):
            PI= self.findPartition(arr,low ,high)
            self.quickSort(arr,low,PI-1)
            self.quickSort(arr,PI+1,high)

arr=[2,1,7,9,0,3,5]
sol=Solution()
sol.quickSort(arr,0,len(arr)-1)
print(arr)

        
