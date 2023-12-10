class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and j < len(popped) and stack[-1] == popped[j] : 
                stack.pop()
                j += 1
        return len(stack) == 0