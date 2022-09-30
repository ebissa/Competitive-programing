class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        i=0
        my_coins=[]
        piles=sorted(piles)
        while i < len(piles):
            temp=[piles[i]]+piles[len(piles)-2:]
            my_coins.append(temp[1])
            i+=1
            piles.pop()
            piles.pop()
        return sum(my_coins)
