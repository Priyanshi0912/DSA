class Solution:
        def merge(self,arr,low,mid,high):  #merging
            temp=[]
            left=low
            right=mid+1
            while(left<=mid and right<=high):
                if (arr[left]<=arr[right]):
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1

            while(left<=mid):
                temp.append(arr[left])
                left+=1
            while(right<=high):
                temp.append(arr[right])
                right+=1


            for i in range(low,high+1):
                arr[i]=temp[i-low]
                
        def mergeSort(self,arr,low,high):  #divinding
            if low>=high:
                return
            mid=(low+high)//2
            self.mergeSort(arr,low,mid)
            self. mergeSort(arr,mid+1,high)
            self.merge(arr,low,mid,high)

arr=[2,6,4,8,9,5,0]
sol=Solution()

sol.mergeSort(arr,0,len(arr)-1)
print(arr)



