from typing import List
from heapq import heappop, heappush

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = []
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        workers.sort()

        ans = float('inf')
        qsum = 0
        pq = []
        for ratio, q in workers:
            qsum += q
            heappush(pq, -q)
            if len(pq) > k:
                qsum += heappop(pq)
            if len(pq) == k:
                ans = min(ans, qsum * ratio)
        return ans
