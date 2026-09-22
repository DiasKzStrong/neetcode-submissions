class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for ss in s:
            if ss not in anagram:
                anagram[ss] = 1
            else:
                anagram[ss] += 1
        second_anagram = {}
        for tt in t:
            if tt not in second_anagram:
                second_anagram[tt] = 1
            else:
                second_anagram[tt] += 1
        return anagram == second_anagram