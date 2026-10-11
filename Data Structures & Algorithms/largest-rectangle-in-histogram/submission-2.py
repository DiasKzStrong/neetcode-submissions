from collections import defaultdict

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > height:
                index, hh = stack.pop()
                area = ((i+1) - (index+1)) * hh
                max_area = max(max_area, area)  
                start = index

            stack.append((start, height))

        for i, h in stack:
            area = ((length+1) - (i+1)) * h
            max_area = max(max_area, area) 

        return max_area