class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            length = min(heights[l], heights[r])
            width = r - l
            curr_vol = length * width

            max_vol = max(curr_vol, max_vol)

            if heights[l] <= heights[r]:
                l += 1

            else: 
                r -= 1

        return max_vol
        