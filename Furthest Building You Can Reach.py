class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        min_heap=[]
        for i in range(n-1):
            diff=heights[i+1]-heights[i]
            if diff>0:
                min_heap.append(diff)
                print(min_heap)
            if len(min_heap)>ladders:
                bricks-=min(min_heap)
                print("bricks remaining:",bricks)
                min_heap.remove(min_heap.index(min(min_heap)))
            if bricks<0:
                return i
        return n-1
