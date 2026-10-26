class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if m > n:
            return ""

        window = [0] * 52
        target = [0] * 52

        for ch in t:
            target[self.find_index(ch)] += 1

        have = 0
        need = sum(1 for freq in target if freq > 0)

        l = 0
        min_len = float("inf")
        start = 0

        for r in range(n):
            s_r_idx = self.find_index(s[r])
            window[s_r_idx] += 1

            if target[s_r_idx] > 0 and window[s_r_idx] == target[s_r_idx]:
                have += 1

            while have == need:
                # Record the minimum valid window
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                s_l_idx = self.find_index(s[l])
                window[s_l_idx] -= 1

                if target[s_l_idx] > 0 and window[s_l_idx] < target[s_l_idx]:
                    have -= 1

                l += 1

        return "" if min_len == float("inf") else s[start:start + min_len]

    def find_index(self, ch: str) -> int:
        if ch.isupper():
            return ord(ch) - ord("A")
        return ord(ch) - ord("a") + 26
