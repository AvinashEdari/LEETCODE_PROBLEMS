class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=int("".join(map(str,digits)))
        y=x+1
        z=list(map(int,str(y)))
        return z

        