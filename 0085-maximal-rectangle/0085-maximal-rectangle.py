class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxArea=max(maxArea,height*(i-index))
                start=index
            stack.append((start,h))
        for i,h in stack:
            maxArea=max(maxArea,h*(len(heights)-i))
        return maxArea
    def maximalRectangle(self, matrix):
        maxArea=0
        heights=[0]*len(matrix[0])
        if not matrix:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            area=self.largestRectangleArea(heights)
            maxArea=max(maxArea,area)
        
        return maxArea

        