class TimeMap:

    def __init__(self):
        self.mp = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""

        arr = self.mp[key]
        l, r = 0, len(arr) - 1
        res = ''

        while l <= r:
            m = (l + r) // 2

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1 
            else:
                r = m - 1
        return res
