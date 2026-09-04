class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            length = min(heights[l], heights[r])
            width = r - l
            curr_water = length * width
            max_water = max(curr_water, max_water)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_water
        