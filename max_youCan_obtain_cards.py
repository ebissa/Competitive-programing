class Solution:
      def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = sum(cardPoints[:k])
        res = left
        for i in range(1, k+1):
            left += cardPoints[-i] - cardPoints[k-i]
            res = max(res, left)
        return res
