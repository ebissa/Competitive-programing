class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans=math.floor((math.sqrt(1+8*n)-1)/2)
        return ans
        