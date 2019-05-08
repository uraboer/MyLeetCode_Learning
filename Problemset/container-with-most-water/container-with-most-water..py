
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: uraboer
# @Date: 2018-10-25 16:29:24
# @Runtime: 168 ms
# @Memory: N/A

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        
        currentMax=0
        
        while l!=r:
            currentMax=max(min(height[r],height[l])*(r-l),currentMax)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
                
        return currentMax
