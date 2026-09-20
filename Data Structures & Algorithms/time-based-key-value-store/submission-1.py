class TimeMap:

    def __init__(self):
        self.hashmap = {}  # key -> list of [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []

        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        values = self.hashmap[key]

        left = 0
        right = len(values) - 1
        res = ""

        # Find largest timestamp <= target timestamp
        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res