import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z|^0-9]', '', s)
        b, l = 0, len(s) - 1

        while b < l:
            s1, s2 = s[b], s[l]

            if s1 != s2:
                return False

            b += 1
            l -= 1
        
        return True