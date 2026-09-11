class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):

        prev = self.right.prev
        cur = self.right

        prev.next = node
        cur.prev = node

        node.prev = prev
        node.next = cur
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        
        node = Node(key, value)
        self.insert(node)
        self.mp[key] = node

        if len(self.mp) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]
            
        

