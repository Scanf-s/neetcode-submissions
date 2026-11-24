import bisect
class TimeMap:

    def __init__(self):
        self.storage: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.storage.keys():
            self.storage[key] = []
        self.storage[key].append((timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.storage.keys():
            return ""
        
        data: list[tuple[int, str]] = self.storage[key]
        start: int = 0
        end: int = len(data) - 1
        candidate: str = ""
        while start <= end:
            mid: int = (start + end) // 2
            if data[mid][0] <= timestamp:
                candidate = data[mid][1]
                start = mid + 1
            else:
                end = mid - 1

        return candidate
