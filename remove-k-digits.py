class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        for n in num:
            while stack and k>0 and n <stack[-1]:
                k-=1
                stack.pop()
            stack.append(n)
        res=stack[:len(stack)-k]
        return str(int("".join(res))) if res else "0"
