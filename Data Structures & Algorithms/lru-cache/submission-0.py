class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.mp = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next  = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key] = Node(key, value)
        self.insert(self.mp[key])

        if len(self.mp) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]


        
