class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        pq=[]
        for i in range(n-1):
            for j in range(i+1,n):
                heappush(pq,(arr[i]/arr[j],(arr[i],arr[j])))
        for _ in range(k):
            a, b = heappop(pq)[1]
        return [a, b]   
