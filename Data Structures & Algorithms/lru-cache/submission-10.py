class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            to_remove = next(iter(self.cache.items()))
            self.cache.pop(to_remove[0])
            self.cache[key] = value