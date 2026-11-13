class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0 for _ in range(len(temperatures))]
        buffer: list[tuple[int, int]] = []
        for idx in range(len(temperatures)):
            while buffer and buffer[-1][0] < temperatures[idx]:
                result[buffer[-1][1]] = idx - buffer[-1][1]
                buffer.pop()
            buffer.append((temperatures[idx], idx))
        return result
        