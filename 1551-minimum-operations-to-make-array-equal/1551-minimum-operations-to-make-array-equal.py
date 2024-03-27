class Solution:
    def minOperations(self, n: int) -> int:
        target = n
        operations = 0
        for i in range(n // 2):
            operations += abs(target - ((i * 2) + 1))
        return operations