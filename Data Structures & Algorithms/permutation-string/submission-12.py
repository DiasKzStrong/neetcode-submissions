from collections import Counter,defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        target = [0] * 26
        window = [0] * 26

        for i in range(m):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if target == window: 
            return True

        for r in range(m, n):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[r - m]) - ord('a')] -= 1
        
            if target == window:
                return True

        return False

        
    