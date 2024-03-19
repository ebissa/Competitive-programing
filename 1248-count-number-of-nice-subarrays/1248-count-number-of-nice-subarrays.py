class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s, ans = 0, 0
        prefixsum = {0:1}
        for num in nums:
            if num & 1:
                s += 1
            if s - k in prefixsum:
                ans += prefixsum[s - k]
            prefixsum[s] = prefixsum.get(s,0) + 1
        return ans