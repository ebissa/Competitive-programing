class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = (arr[i-1] > arr[i]) - (arr[i-1] < arr[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * ((arr[i] > arr[i+1]) - (arr[i] < arr[i+1])) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
