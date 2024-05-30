class Solution:
    def arrangeCoins(self, n: int) -> int:
        root=math.sqrt(1+8*n)
        ans=math.floor((root-1)/2)
        return ans
        