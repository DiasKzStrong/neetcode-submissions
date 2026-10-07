import operator

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in ["+","-","*","/"]:
                b, a = stack.pop(), stack.pop()
                res = ops[token](a,b)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()