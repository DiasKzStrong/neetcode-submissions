from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        counter = Counter() 
        buckets = [[] for _ in range(length+1)]

        for num in nums:
            counter[num] += 1  

        for num,v in counter.items():
            buckets[v].append(num)

        res = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
    