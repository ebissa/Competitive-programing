class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                temp=""
                while stack and stack[-1]!='[':
                    temp=stack.pop()+temp
                stack.pop()
                digits=""
                while stack and stack[-1].isdigit():
                    digits=stack.pop()+digits
                stack.append(int(digits)*temp)
        return ''.join(stack)