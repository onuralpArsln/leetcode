class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea=0

        while( right > left):
            currentArea = min(height[left],height[right]) * (right-left)
            maxArea = max(currentArea,maxArea)

            if height[right] > height[left]:
                left=left+1
            else:
                right = right -1 

        return maxArea


        