def ceil(arr: [int], n: int, x: int) -> int:
    # Write your code here
    ans=-1
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=arr[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
    pass

def floor(arr: [int], n: int, x: int) -> int:
    # Write your code here
    ans=-1
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=x:
            ans=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
    pass

def getFloorAndCeil(a, n, x):
    return floor(a,n,x), ceil(a,n,x)
    

    # Write your code here. 
