class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        m = len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]  # Initialize the rotated matrix
        
        # Rotate each element
        for i in range(n):
            for j in range(m):
                new_j = (j - k) % m  # Calculate new column index after rotation
                ans[i][new_j] = mat[i][j]  # Place the element in the rotated position
        
        return ans

                
        # code here

