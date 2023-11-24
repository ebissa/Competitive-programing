class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for operation in operations:
            if stack:
                if operation=="+":
                    stack.append(int(stack[-1]) +int(stack[-2]))
                elif operation=="D":
                    stack.append(int(stack[-1])*2)
                elif operation=="C":
                    stack.pop()
                else:
                    stack.append(int(operation))
            else:
                stack.append(int(operation))
        return sum(stack)

        