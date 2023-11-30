class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        prev = [0] * len(arr)
        _next = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            prev[i]=stack[-1] if stack else -1
            stack.append(i)
        stack =[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[i]<arr[stack[-1]]:
                stack.pop()
            _next[i]=stack[-1] if stack else len(arr)
            stack.append(i)
        return sum(((i-prev[i])*(_next[i]-i)*arr[i] for i in range(len(arr)) ))%MOD