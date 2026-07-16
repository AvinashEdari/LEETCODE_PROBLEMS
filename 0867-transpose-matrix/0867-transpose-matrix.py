class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        ans=[]
        for i in range(c):
            l=[]
            for j in  range(r):
                l.append(matrix[j][i])
            ans.append(l)
        return ans
        