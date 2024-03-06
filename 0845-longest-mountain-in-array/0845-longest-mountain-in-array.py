class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        longest = 0
        left = 0
        while left < n:
            right = left
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1
            peak = right
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            if peak != left and peak != right:
                longest = max(longest, right - left + 1)
            left = max(left + 1, right)

        return longest
