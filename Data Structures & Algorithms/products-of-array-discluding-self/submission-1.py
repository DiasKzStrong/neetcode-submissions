from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0 for _ in range(length)]
        suffix = [0 for _ in range(length)]
        res = [0 for _ in range(length)]

        prefix[0] = suffix[length - 1] = 1

        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(length-2, -1, -1):
            suffix[j] = nums[j+1] * suffix[j+1]

        for i in range(length):
            res[i] = prefix[i] * suffix[i]
        
        return res