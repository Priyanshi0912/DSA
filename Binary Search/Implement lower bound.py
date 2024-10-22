def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    ans=n
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
    pass
