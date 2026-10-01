class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        stack = []
        rules = {
            "[":"]",
            "{":"}",
            "(":")"
        }

        for br in s:
            if br in "[({":
                stack.append(br)
            else:
                if not stack: 
                    return False
                last = stack.pop()  
                if rules[last] != br:
                    return False

        if stack:
            return False 
        return True