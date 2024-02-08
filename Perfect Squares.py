from typing import List

class Solution:
    def solve(self, n: int, memo: List[int]):
        if n == 0:
            return 0
        if n < 0:
            return float("inf")
        if memo[n] != -1:
            return memo[n]
        mini = n
        i = 1
        while i * i <= n:
            mini = min(mini, 1 + self.solve(n - (i * i), memo))
            i += 1
        memo[n] = mini
        return memo[n]

    def numSquares(self, n: int) -> int:
        memo = [-1] * (n + 1)
        return self.solve(n, memo)
