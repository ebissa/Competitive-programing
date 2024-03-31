class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        res, max_first, max_second = prefix_sum[firstLen + secondLen], prefix_sum[firstLen], prefix_sum[secondLen]

        for i in range(firstLen + secondLen + 1, len(prefix_sum)):
            max_first = max(max_first, prefix_sum[i - secondLen] - prefix_sum[i - secondLen - firstLen])
            max_second = max(max_second, prefix_sum[i - firstLen] - prefix_sum[i - firstLen - secondLen])

            res = max(res, max_first + prefix_sum[i] - prefix_sum[i - secondLen], max_second + prefix_sum[i] - prefix_sum[i - firstLen])

        return res