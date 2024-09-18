class Solution:
    def swap(self,arr,ind1,ind2):
        temp=arr[ind1]
        arr[ind1]=arr[ind2]
        arr[ind2]=temp
    def selectionSort(self,arr):
        n=len(arr)
        for i in range(0,n-1):
            mini=i   
            for j in range(i,n):
                if (arr[j]<arr[mini]):
                    mini=j

            self.swap(arr,mini,i)
        

arr=[8,3,1,0,9,2,1]
sol=Solution()
sol.selectionSort(arr)
print(arr)
