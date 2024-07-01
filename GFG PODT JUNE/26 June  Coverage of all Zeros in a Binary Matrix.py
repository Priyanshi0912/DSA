

class Solution:
    def findCoverage(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i - 1 >= 0 and matrix[i - 1][j] == 1:  # Check top neighbor
                        ans += 1
                    if i + 1 < n and matrix[i + 1][j] == 1:  # Check bottom neighbor
                        ans += 1
                    if j - 1 >= 0 and matrix[i][j - 1] == 1:  # Check left neighbor
                        ans += 1
                    if j + 1 < m and matrix[i][j + 1] == 1:  # Check right neighbor
                        ans += 1
        
        return ans

        # Code here
