# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = float('-inf')

        second = head
        fast = head

        while fast and fast.next:
            second = second.next
            fast = fast.next.next

        pnode, curr = None, second

        while curr:
            nnode = curr.next
            curr.next = pnode
            pnode = curr
            curr = nnode

        while pnode and head:
            max_sum = max(max_sum, pnode.val + head.val)
            pnode = pnode.next
            head = head.next

        return max_sum