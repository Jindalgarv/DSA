from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.stack = deque()
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        self.stack.remove(key)      # remove old position
        self.stack.append(key)      # mark as recently used

        return self.d[key]

    def put(self, key: int, value: int) -> None:

        if key in self.d:
            self.stack.remove(key)

        self.d[key] = value
        self.stack.append(key)

        if len(self.d) > self.capacity:
            lru = self.stack.popleft()
            del self.d[lru]