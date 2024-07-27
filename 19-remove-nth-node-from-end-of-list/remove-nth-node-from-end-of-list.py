# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode()
        dum.next = head
        a = b = dum

        for _ in range(n + 1):
            a = a.next
        
        while a:
            b = b.next
            a = a.next
        
        b.next = b.next.next # This is the removal part
        return dum.next