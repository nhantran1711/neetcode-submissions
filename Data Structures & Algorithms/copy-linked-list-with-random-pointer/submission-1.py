"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mp = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            mp[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copyNode = mp[cur]
            copyNode.next = mp[cur.next]
            copyNode.random = mp[cur.random]
            cur = cur.next
        return mp[head]