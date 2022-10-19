class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackI=stack.pop()
                res[stackI]=(i-stackI)
            stack.append([t,i])
        return res
