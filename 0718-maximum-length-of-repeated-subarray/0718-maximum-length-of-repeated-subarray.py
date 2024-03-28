from collections import defaultdict

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            k = 0
            for j in range(length):
                if nums1[i + j] == nums2[j]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
        for i in range(m):
            length = min(n, m - i)
            k = 0
            for j in range(length):
                if nums1[j] == nums2[i + j]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
        return ret