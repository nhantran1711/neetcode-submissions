# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    

        dummy = ListNode(0)
        dummy.next = head

        prevGroup = dummy

        while True:
            kth = self.getKthNode(prevGroup, k)
            if not kth:
                break
            
            nextGroup = kth.next

            cur = prevGroup.next
            prev = kth.next

            while cur !=  nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
            
        return dummy.next
            

    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur