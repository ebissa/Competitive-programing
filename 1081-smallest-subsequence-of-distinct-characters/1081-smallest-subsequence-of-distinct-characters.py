class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occerance={c:i for i,c in enumerate(s)}
        stack=[]
        for i,c in enumerate(s):
            if c not in stack:
                while stack and c<stack[-1] and i <last_occerance[stack[-1]]:
                    stack.pop()
                stack.append(c)
        return "".join(stack)
        
