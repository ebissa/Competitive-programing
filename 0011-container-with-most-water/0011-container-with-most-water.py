class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l=0
        r=len(height)-1
        while l<r:
            if height[l]<=height[r]:
                temp_area=height[l]*(r-l)
                max_area=max(max_area,temp_area)
                l+=1
            else:
                temp_area=height[r]*(r-l)
                max_area=max(max_area,temp_area)
                r-=1
        return max_area
        