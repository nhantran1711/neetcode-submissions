# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # [1, 2, 3, 4] n = 1
               
        #        temp = cur.next
        #        cur.next = temp.next
        #        temp.next = None

        # index = length - n - 1 # 

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        index = length - n - 1
        if index <= -1:
            return head.next
        
        cur = head
        i = 0
        while i != index:
            cur = cur.next
            i += 1
        
        temp = cur.next
        cur.next = temp.next
        temp.next = None

        return head
        


