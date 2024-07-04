class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l , r = 0,len(height) - 1

        while l < r:
            area = (r - l)*min([height[r],height[l]])
            if max_area < area:
                max_area = area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
            
        return max_area
      