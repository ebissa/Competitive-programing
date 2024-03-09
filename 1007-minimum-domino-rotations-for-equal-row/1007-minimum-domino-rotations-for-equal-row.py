class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        nlen = len(tops)
        topC = Counter(tops)
        bottomC = Counter(bottoms)
        totalC = topC + bottomC

        num, freq = totalC.most_common()[0]

        for i in range(nlen):
            if num != tops[i] and num != bottoms[i]:
                return -1

        return nlen-max(topC[num], bottomC[num])