from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        remaining_unique = len(counts)
        sorted_counts = sorted(counts.values())
        
        for count in sorted_counts:
            if k >= count:
                k -= count
                remaining_unique -= 1
            else:
                break
        
        return remaining_unique
