from collections import defaultdict

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        distinct_heights = set(heights)
        occupancy = defaultdict(int)
    
        for d_h in distinct_heights:
            length = 0
            max_length = 0
            for h in heights:
                if d_h <= h:
                    length += 1
                else:
                   max_length = max(length, max_length)
                   length = 0
            max_length = max(length, max_length)
            occupancy[d_h] = max_length

        res = 0
        for k,v in occupancy.items():
            curr = k * v
            if res < curr:
                res = curr
            
        return res