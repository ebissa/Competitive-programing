class Solution:
    def evalRPN(self, tokens: list[str]):
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                second_num = int(stack.pop())
                first_num= int(stack.pop())
                if token == '+':
                    output = second_num + first_num
                elif token == '-':
                    output = first_num - second_num
                elif token == '*':
                    output = first_num * second_num
                else:
                    output = int(first_num/second_num)
                stack.append(output)
                
        return stack[0]
            
