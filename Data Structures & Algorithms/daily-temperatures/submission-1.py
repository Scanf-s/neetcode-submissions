class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0 for _ in range(len(temperatures))]
        buffer: list[int] = []
        for idx in range(len(temperatures)):
            while buffer and temperatures[buffer[-1]] < temperatures[idx]:
                result[buffer[-1]] = idx - buffer[-1]
                buffer.pop()
            buffer.append(idx)
        return result
        