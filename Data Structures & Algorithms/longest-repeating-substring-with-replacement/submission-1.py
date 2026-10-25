from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for _ in range(26)]
        res = 0
        l = 0

        for r in range(len(s)):
            
            length = r - l + 1
            count[self.find_index(s[r])] += 1

            if count and length - max(count) > k:
                count[self.find_index(s[l])] -= 1
                l += 1

            res = max(res, r - l + 1)


        return res

    def find_index(self, ch: str) -> int:
        return ord(ch) - ord('A')
