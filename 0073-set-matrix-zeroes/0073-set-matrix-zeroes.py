class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        r={}
        c={}
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    r[i]=True
                    c[j]=True
        for i in range(row):
            for j in range(col):
                if i in r or j in c:
                    matrix[i][j]=0
        return matrix