import heapq
class MinStack:

    def __init__(self):
        self.buffer: list[int] = []
        self.minheap: list[int] = []

    def push(self, val: int) -> None:
        self.buffer.append(val)
        heapq.heappush(self.minheap, val)

    def pop(self) -> None:
        cur_top: int = self.buffer[-1]
        self.buffer.pop()
        self.minheap.remove(cur_top)
        heapq.heapify(self.minheap)

    def top(self) -> int:
        return self.buffer[-1]

    def getMin(self) -> int:
        return self.minheap[0]
