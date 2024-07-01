class Solution:
    def pattern (self, arr):
        rows = len(arr)
        cols = len(arr[0])
        find=False
        for row in range(rows):
            if arr[row]==arr[row][::-1]:
                ans=(str(row) + " " + "R")
                find=True
                break
        if find==False:
            for col in range(cols):
                column = [arr[row][col] for row in range(rows)]
                if column==column[::-1]:
                    find=True
                    ans=(str(col)+" "+"C")
                    break
        if find :
            return ans
        else:
            return -1
