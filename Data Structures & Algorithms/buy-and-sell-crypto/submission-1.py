class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1

        res = 0 

        while r <= len(prices) - 1:

            while l < r:
                profit = prices[r] - prices[l]
                res = max(res, profit)
                l += 1

            r += 1
            l = 0 

        return res