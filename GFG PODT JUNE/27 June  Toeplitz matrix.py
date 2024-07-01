
def isToepliz(mat):
    n=len(mat)
    m=len(mat[0])
    temp=mat[0][0]
    ans=True
    for i in range(n):
        for j in range(m):
            if (i==j and mat[i][j]!=temp):
                ans=False
    if ans:
        return 1
    else:
        return 0
    #code here
