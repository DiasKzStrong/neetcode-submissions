class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: 
            return 0

        total = 0   
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            
            if max_l < max_r or max_l == max_r:
                l += 1 
                h = height[l]
                w_t = max_l - h 
                total += w_t if w_t > 0 else 0
                max_l = max(max_l, h)
            elif max_l > max_r:
                r -= 1
                h = height[r]
                w_t = max_r - h 
                total += w_t if w_t > 0 else 0
                max_r = max(max_r, h)

        return total
