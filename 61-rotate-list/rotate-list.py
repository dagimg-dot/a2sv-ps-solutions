# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        nodes = []
        count, curr = 0, head

        while curr:
            nodes.append(curr)
            curr = curr.next
            count += 1

        if count == 1:
            return head

        k = k % count
        if k == 0:
            return head

        nodes[-k-1].next = None
        nodes[-1].next = nodes[0]

        return nodes[-k]