from collections import Counter,defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_l = len(s1)

        print(s2[:w_l])

        if Counter(s1) == Counter(s2[:w_l]):
            return True

        for i in range(1, len(s2)):
            
            if Counter(s1) == Counter(s2[i: w_l + i]):
                return True

        return False 
