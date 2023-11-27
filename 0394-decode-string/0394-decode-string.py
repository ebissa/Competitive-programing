class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp_str=""
                while stack[-1] != '[':
                    stack_top=stack.pop()
                    temp_str = stack_top + temp_str
                stack.pop()
                digital=""
                while stack and stack[-1].isdigit():
                    stack_top=stack.pop()
                    digital = stack_top + digital
                stack.append(int(digital)*temp_str)
        return "".join(stack)