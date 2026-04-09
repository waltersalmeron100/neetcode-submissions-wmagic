class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        tuple_stack = []

        for c_index, c_height in enumerate(heights):
            s_index = c_index
            while tuple_stack and tuple_stack[-1][1] > c_height:
                pop_index, pop_height = tuple_stack.pop()
                max_area = max(max_area, pop_height * (c_index - pop_index))
                s_index = pop_index
            tuple_stack.append((s_index, c_height))

        for index, height in tuple_stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area
        