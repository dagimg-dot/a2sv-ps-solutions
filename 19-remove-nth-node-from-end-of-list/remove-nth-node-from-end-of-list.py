# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        a = b = dummy

        for _ in range(n + 1):
            a = a.next
        
        while a:
            b = b.next
            a = a.next
        
        b.next = b.next.next 
        return dummy.next