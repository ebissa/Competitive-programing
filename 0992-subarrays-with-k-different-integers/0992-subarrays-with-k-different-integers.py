class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            freq = defaultdict(int)
            left, count = 0, 0

            for right in range(len(nums)):
                freq[nums[right]] += 1

                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                count += right - left + 1

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)
        