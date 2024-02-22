class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        incoming= defaultdict(int)
        outgoing=defaultdict(int)
        for i,j in trust:
            incoming[j]+=1
            outgoing[i]+=1
        for i,j in incoming.items():
            if j==n-1 and outgoing[i]==0:
                return i
        return -1
