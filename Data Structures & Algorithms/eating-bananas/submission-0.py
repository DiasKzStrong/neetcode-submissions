class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ = max(piles)
        l, r = 1, max_

        res = float('inf')
        while l <= r:
            total = 0
            k = l + ((r - l) // 2)
            for p in piles:
                total += math.ceil(p / k)
        
            if total > h:
                l = k + 1
            elif total <= h:
                r = k - 1
                res = min(res,k)
        return res



    