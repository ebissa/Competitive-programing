class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_area=height[i]*i
        while i<j:
            if height[i]<=height[j]:
                temp_area=height[i]*(j-i)
                max_area=max(temp_area,max_area)
                i+=1
            else:
                temp_area=height[j]*(j-i)
                max_area=max(temp_area,max_area)
                j-=1
        return max_area
