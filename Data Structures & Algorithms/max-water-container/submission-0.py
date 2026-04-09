class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            current_area = (r - l) * min(heights[l], heights[r])

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            if max_area < current_area:
                max_area = current_area

        return max_area
        