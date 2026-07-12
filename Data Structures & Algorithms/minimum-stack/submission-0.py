class MinStack:

    def __init__(self):
        self.data = []
        self.minEl = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        minEl = min(self.data)
        return minEl
