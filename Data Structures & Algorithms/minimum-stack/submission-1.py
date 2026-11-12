class MinStack:

    def __init__(self):
        self.buffer: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.buffer.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.buffer.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.buffer[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]