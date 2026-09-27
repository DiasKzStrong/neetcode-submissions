class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = len(s)
            if length > 99:
                res.append(f"t{length}#{s}")
            elif length > 9:
                res.append(f"d{length}#{s}")
            else:
                res.append(f"{length}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        max_length = len(s)
        while i < max_length:
            if s[i] == "t":
                length = int(s[i+1:i+4])
                i += 3
            elif s[i] == "d":
                length = int(s[i+1:i+3])
                i += 2
            else:
                length = int(s[i])
            res.append(s[i+2:i+2+length])
            i += length + 2
        return res