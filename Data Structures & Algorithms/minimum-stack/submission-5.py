class MinStack:

    def __init__(self):
        self.data = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        if not self.data:
            raise ValueError()

        self.data.pop()
        self.minStack.pop()

    
    def top(self) -> int:
        if not self.data:
            raise ValueError()
        return self.data[-1]

    def getMin(self) -> int:
        if not self.data:
            raise ValueError()
        return self.minStack[-1]
        
