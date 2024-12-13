from sortedcontainers import SortedDict

class TreeMap:
    
    def __init__(self):
        self.map = SortedDict()

    def insert(self, key: int, val: int) -> None:
        self.map[key] = val

    def get(self, key: int) -> int:
        return self.map.get(key, -1)

    def getMin(self) -> int:
        if not self.map:
            return -1
        mk = min(list(self.map.keys())) # smallest key
        return self.map[mk]


    def getMax(self) -> int:
        if not self.map:
            return -1
        max_key = max(list(self.map.keys()))
        return self.map[max_key]

    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]

    def getInorderKeys(self) -> List[int]:
        return sorted(list(self.map.keys()))
