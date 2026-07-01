class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = [float("inf")]

    def push(self, val: int) -> None:
        if val <= self.mins[-1]: 
            self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]: 
            self.mins.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
