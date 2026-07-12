class MinStack:

    def __init__(self):
        self.data = []
        self.minEl = []

    def push(self, val: int) -> None:
        self.data.append(val)

        if not self.minEl:
            self.minEl.append(val)
            
        else:
            self.minEl.append(min(val, self.minEl[-1]))

    def pop(self) -> None:
        self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return min(self.data)
