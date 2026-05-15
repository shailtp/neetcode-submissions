class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_area=0

        while left<right:
            curr_area=(right-left)*min(heights[right], heights[left])
            max_area=max(max_area, curr_area)

            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1

        return max_area

        #Time: O(n), space: O(1)
        