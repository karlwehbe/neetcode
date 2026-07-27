class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0

        print("initializing with capacity =", capacity)

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
        elif self.count < self.capacity:
            self.cache[key] = value
            self.count += 1
        else:
            to_remove = next(iter(self.cache.items()))
            self.cache.pop(to_remove[0])
            self.cache[key] = value