class Solution(object):
    def addToArrayForm(self, num, k):
         x=int(''.join(map(str,num)))
         y=x+k
         z=list(map(int,str(y)))
         return z
        