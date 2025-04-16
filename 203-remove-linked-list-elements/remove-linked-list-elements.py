# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p_node, curr = dummy, head

        while curr:
            if curr.val == val:
                p_node.next = curr.next
            else:
                p_node = curr
            
            curr = curr.next

            
        return dummy.next