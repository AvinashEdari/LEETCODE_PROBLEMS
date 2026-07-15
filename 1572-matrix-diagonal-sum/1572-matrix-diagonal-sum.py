class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sum1=0
        for i in range(n):
            sum1+=mat[i][i]+mat[i][n-1-i]
        if n%2==0:
            return sum1
        else:
            sum1-=mat[n//2][n//2]
            return sum1
