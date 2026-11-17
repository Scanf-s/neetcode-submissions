class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result: int = 0
        arrival_time: dict[int, float] = {}
        for pos, sp in zip(position, speed):
            arrival_time[pos] = (target - pos) / sp

        arrival_buffer: list[tuple[int, float]] = sorted(arrival_time.items())
        while arrival_buffer:
            cur: tuple[int, float] = arrival_buffer.pop()
            while arrival_buffer and arrival_buffer[-1][1] <= cur[1]:
                arrival_buffer.pop()
            
            result += 1
        
        return result
            