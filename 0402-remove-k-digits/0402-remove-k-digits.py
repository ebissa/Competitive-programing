class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        for n in num:
            while stack and k>0 and n <stack[-1]:
                k-=1
                stack.pop()
            stack.append(n)
        res=stack[:len(stack)-k]
        res = "".join(res).lstrip('0')
        return res if res else "0"