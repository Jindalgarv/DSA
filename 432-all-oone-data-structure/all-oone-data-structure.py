class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.mp = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node, new):
        new.prev = node
        new.next = node.next
        node.next.prev = new
        node.next = new

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.mp:
            if self.head.next.count != 1:
                self.insert(self.head, Node(1))
            node = self.head.next
            node.keys.add(key)
            self.mp[key] = node
            return

        node = self.mp[key]

        if node.next.count != node.count + 1:
            self.insert(node, Node(node.count + 1))

        nxt = node.next
        nxt.keys.add(key)
        self.mp[key] = nxt

        node.keys.remove(key)
        if not node.keys:
            self.remove(node)

    def dec(self, key):
        node = self.mp[key]

        if node.count == 1:
            del self.mp[key]
        else:
            if node.prev.count != node.count - 1:
                self.insert(node.prev, Node(node.count - 1))

            prev = node.prev
            prev.keys.add(key)
            self.mp[key] = prev

        node.keys.discard(key)

        if not node.keys:
            self.remove(node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))